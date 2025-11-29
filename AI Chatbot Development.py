import streamlit as st
from streamlit_webrtc import webrtc_streamer, AudioProcessorBase, WebRtcMode
import google.generativeai as genai
import speech_recognition as sr
import numpy as np
import tempfile
import av
import time
import wave

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="NEXUS AI Chat", page_icon="🤖", layout="centered")

# -------------- AUDIO PROCESSOR ----------------
class AudioProcessor(AudioProcessorBase):
    def __init__(self):
        self.frames = []

    def recv_audio(self, frame: av.AudioFrame) -> av.AudioFrame:
        audio = frame.to_ndarray().flatten().astype(np.float32)
        self.frames.append(audio)
        return frame

# -------------- SIDEBAR ----------------
with st.sidebar:
    st.header("⚙️ Configurations")
    api_key = st.text_input("Enter Google API Key", type="password")
    model_name = st.selectbox("Gemini Model", ["gemini-2.5-flash", "gemini-pro", "gemini-1.5-pro"])
    max_tokens = st.slider("Max Tokens", 50, 2000, 700)

# -------------- TITLE ----------------
st.title("🤖 NEXUS AI Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Show chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# ------------------ VOICE INPUT -------------------
st.subheader("🎤 Speak to NEXUS")

webrtc_ctx = webrtc_streamer(
    key="voice",
    mode=WebRtcMode.SENDONLY,
    audio_processor_factory=AudioProcessor,
    media_stream_constraints={"audio": True, "video": False},
)

voice_text = None

if webrtc_ctx and webrtc_ctx.audio_processor:
    if st.button("Convert Voice to Text"):
        frames = webrtc_ctx.audio_processor.frames

        if len(frames) > 0:
            audio_data = np.concatenate(frames)

            # ----- Save PCM as WAV correctly -----
            with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
                with wave.open(temp_audio.name, 'wb') as wav_file:
                    wav_file.setnchannels(1)
                    wav_file.setsampwidth(2)
                    wav_file.setframerate(16000)
                    wav_file.writeframes((audio_data * 32767).astype(np.int16).tobytes())
                audio_path = temp_audio.name

            # ----- Speech Recognition -----
            r = sr.Recognizer()
            with sr.AudioFile(audio_path) as src:
                audio_data = r.record(src)
                try:
                    voice_text = r.recognize_google(audio_data)
                    st.success(f"Recognized: **{voice_text}**")
                except:
                    st.error("Speech not recognized.")
        else:
            st.warning("No audio detected! Try speaking again.")

# --------------- TEXT INPUT ----------------
prompt = st.chat_input("Type your message...")

if voice_text:
    prompt = voice_text  # voice overrides text input

if prompt:

    if not api_key:
        st.warning("Please enter your API key!")
        st.stop()

    # store user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel(model_name)

        with st.chat_message("assistant"):
            with st.spinner("NEXUS is thinking..."):
                response = model.generate_content(
                    prompt,
                    generation_config={"max_output_tokens": max_tokens}
                )
                reply = response.text
                st.write(f"### 🤖 NEXUS:\n{reply}")

        st.session_state.messages.append({"role": "assistant", "content": reply})
        time.sleep(0.2)
        st.rerun()

    except Exception as e:
        st.error(f"Error: {e}")
