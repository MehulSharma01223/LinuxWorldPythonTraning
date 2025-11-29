import pyttsx3

def text_to_speech():
    engine = pyttsx3.init()

    # Set voice speed (optional)
    engine.setProperty('rate', 170)

    # Set volume (0.0 to 1.0)
    engine.setProperty('volume', 1.0)

    # List available voices
    voices = engine.getProperty('voices')
    print("\nAvailable Voices:")
    for i, voice in enumerate(voices):
        print(f"{i}. {voice.name}")

    choice = int(input("\nChoose voice number: "))
    engine.setProperty('voice', voices[choice].id)

    # Take text input
    text = input("\nEnter text to speak: ")

    print("\nSpeaking... 🔊")
    engine.say(text)
    engine.runAndWait()


# Run program
text_to_speech()
