import streamlit as st
from datetime import datetime
import qrcode
import io

# ----------------- PAGE CONFIG -----------------
st.set_page_config(
    page_title="WashHubb Smart Laundry",
    page_icon="",
    layout="wide"
)

# ----------------- LOGIN SYSTEM -----------------
VALID_USERNAME = "admin"
VALID_PASSWORD = "admin123"


def login_page():
    st.title("WashHubb – Login ")
    st.write("Enter your username and password to continue.")

    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        login_btn = st.form_submit_button("Login")

    if login_btn:
        if username == VALID_USERNAME and password == VALID_PASSWORD:
            st.session_state.logged_in = True
            st.success("Login successful! Redirecting to dashboard...")
            st.rerun()  # works in latest Streamlit
        else:
            st.error("Incorrect username or password ❌")


# Initialize login state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# If not logged in -> show login and stop
if not st.session_state.logged_in:
    login_page()
    st.stop()

# ----------------- CUSTOM CSS -----------------
st.markdown(
    """
    <style>
    .main {
        background: #f5f9ff;
    }
    h1, h2, h3, h4 {
        font-family: "Segoe UI", system-ui, sans-serif;
    }
    .hero-title {
        font-size: 2.5rem;
        font-weight: 800;
        line-height: 1.1;
        margin-bottom: 0.5rem;
    }
    .hero-subtitle {
        font-size: 1.05rem;
        color: #4c5a70;
        margin-bottom: 1.5rem;
    }
    .pill {
        display: inline-block;
        padding: 0.3rem 0.8rem;
        border-radius: 999px;
        background: #e0f2ff;
        color: #0369a1;
        font-size: 0.8rem;
        font-weight: 600;
        letter-spacing: 0.04em;
        text-transform: uppercase;
        margin-bottom: 0.8rem;
    }
    .secondary-btn {
        border-radius: 999px;
        padding: 0.6rem 1.4rem;
        border: 1px solid #cbd5f5;
        font-weight: 500;
        font-size: 0.9rem;
        margin-left: 0.6rem;
    }
    .pricing-card {
        background: white;
        padding: 1.2rem 1.2rem 1.4rem 1.2rem;
        border-radius: 1.4rem;
        border: 1px solid #e2e8f0;
        box-shadow: 0 12px 30px rgba(15, 23, 42, 0.06);
        height: 100%;
    }
    .pricing-price {
        font-size: 1.6rem;
        font-weight: 800;
        color: #0f172a;
    }
    .pricing-period {
        font-size: 0.85rem;
        color: #6b7280;
    }
    .footer {
        text-align: center;
        font-size: 0.78rem;
        color: #64748b;
        padding: 1.5rem 0 0.5rem 0;
        margin-top: 2rem;
        border-top: 1px dashed #cbd5f5;
    }
    .metric-label {
        font-size: 0.8rem;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        color: #64748b;
        font-weight: 600;
    }
    .metric-value {
        font-size: 1.4rem;
        font-weight: 800;
        color: #0f172a;
    }
    .metric-sub {
        font-size: 0.8rem;
        color: #94a3b8;
    }
    .tag {
        display: inline-block;
        padding: 0.2rem 0.7rem;
        border-radius: 999px;
        background: #e2fbe8;
        color: #15803d;
        font-size: 0.75rem;
        font-weight: 600;
        margin-right: 0.3rem;
        margin-bottom: 0.3rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ----------------- SIDEBAR -----------------
try:
    st.sidebar.image(
        "logo.png",              # optional logo file in same folder
        use_container_width=True
    )
except Exception:
    st.sidebar.write(" WashHubb")

st.sidebar.markdown("### WashHubb Smart Laundry")
st.sidebar.markdown("Tech-enabled laundry for Hostels & PGs")

page = st.sidebar.radio(
    "Navigate",
    ["Home", "Services & Pricing", "Book a Wash", "About & Contact"]
)

st.sidebar.markdown("---")
if st.sidebar.button("Logout"):
    st.session_state.logged_in = False
    st.rerun()

st.sidebar.caption("Built with  using Streamlit")

# ----------------- PAGES -----------------

# HOME PAGE
if page == "Home":
    col1, col2 = st.columns([1.3, 1])

    with col1:
        st.markdown('<div class="pill">SMART LAUNDRY FOR STUDENTS</div>', unsafe_allow_html=True)
        st.markdown('<div class="hero-title">Laundry made as easy as a QR scan.</div>', unsafe_allow_html=True)
        st.markdown(
            '<p class="hero-subtitle">'
            'WashHubb installs smart washing & ironing stations inside hostels and PGs. '
            'Students scan, pay, and wash in minutes – no more waiting for the dhobi.'
            '</p>',
            unsafe_allow_html=True
        )

        bcol1, bcol2 = st.columns([0.4, 0.6])
        with bcol1:
            st.button(" Book a Wash Now", key="book_btn")
        with bcol2:
            st.markdown('<button class="secondary-btn">View pricing →</button>', unsafe_allow_html=True)

        st.write("")
        mc1, mc2, mc3 = st.columns(3)
        with mc1:
            st.markdown('<div class="metric-label">CHEAPER THAN DHOBI</div>', unsafe_allow_html=True)
            st.markdown('<div class="metric-value">3x</div>', unsafe_allow_html=True)
            st.markdown('<div class="metric-sub">on average per month</div>', unsafe_allow_html=True)
        with mc2:
            st.markdown('<div class="metric-label">PER WASH FROM</div>', unsafe_allow_html=True)
            st.markdown('<div class="metric-value">₹99</div>', unsafe_allow_html=True)
            st.markdown('<div class="metric-sub">5 kg student load</div>', unsafe_allow_html=True)
        with mc3:
            st.markdown('<div class="metric-label">TIME SAVED</div>', unsafe_allow_html=True)
            st.markdown('<div class="metric-value">5+ hrs</div>', unsafe_allow_html=True)
            st.markdown('<div class="metric-sub">per week per student</div>', unsafe_allow_html=True)

    with col2:
        # Optional hero image
        try:
            st.image(
                "hero_laundry.png",
                caption="On-site smart washing machines with QR-pay.",
                use_container_width=True
            )
        except Exception:
            st.info("Add 'hero_laundry.png' in the folder to show hero image.")

    st.markdown("### Why students love WashHubb")
    f1, f2, f3, f4 = st.columns(4)
    with f1:
        st.markdown(" **On-site machines**  \nNo more walking to market laundry.")
    with f2:
        st.markdown(" **Up to 3x cheaper**  \nTransparent pricing, no surprise bills.")
    with f3:
        st.markdown(" **Scan → Pay → Wash**  \nFully digital using QR & UPI.")
    with f4:
        st.markdown(" **Eco-friendly**  \nEnergy-efficient machines & detergents.")

    st.markdown("### How it works")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("**1. Scan the QR**  \nChoose a machine and scan its QR from the app.")
    with c2:
        st.markdown("**2. Select service**  \nWash / Wash + Dry / Ironing, pick cycle & pay.")
    with c3:
        st.markdown("**3. Get notified**  \nRelax! Get a notification when your clothes are ready.")

# SERVICES & PRICING
elif page == "Services & Pricing":
    st.header("Services & Pricing ")

    col_wash, col_washdry, col_iron = st.columns(3)

    with col_wash:
        st.markdown('<div class="pricing-card">', unsafe_allow_html=True)
        st.subheader("Wash Only")
        st.markdown('<div class="pricing-price">₹99</div>', unsafe_allow_html=True)
        st.markdown('<div class="pricing-period">per 5 kg load</div>', unsafe_allow_html=True)
        st.markdown("• Ideal for daily / hostel wear\n"
                    "• Standard detergent & softener\n"
                    "• 30–40 min cycle")
        st.markdown('</div>', unsafe_allow_html=True)

    with col_washdry:
        st.markdown('<div class="pricing-card">', unsafe_allow_html=True)
        st.subheader("Wash + Dry")
        st.markdown('<div class="pricing-price">₹149</div>', unsafe_allow_html=True)
        st.markdown('<div class="pricing-period">per 5 kg load</div>', unsafe_allow_html=True)
        st.markdown("• Wash + tumble dry\n"
                    "• Ready-to-fold clothes\n"
                    "• Perfect for monsoon season")
        st.markdown('</div>', unsafe_allow_html=True)

    with col_iron:
        st.markdown('<div class="pricing-card">', unsafe_allow_html=True)
        st.subheader("Ironing")
        st.markdown('<div class="pricing-price">₹19</div>', unsafe_allow_html=True)
        st.markdown('<div class="pricing-period">per session</div>', unsafe_allow_html=True)
        st.markdown("• 5–6 clothes per session\n"
                    "• 20 min average time\n"
                    "• Crisp formals & uniforms")
        st.markdown('</div>', unsafe_allow_html=True)

# BOOK A WASH (WITH QR)
elif page == "Book a Wash":
    st.header("Book a Wash ")
    st.info("Demo booking form. In production, connect this to a database or backend API.")

    with st.form("wash_booking_form"):
        c1, c2 = st.columns(2)
        with c1:
            name = st.text_input("Full Name")
            phone = st.text_input("Mobile Number")
            hostel = st.text_input("Hostel / PG Name")
            room = st.text_input("Room Number")
        with c2:
            service_type = st.selectbox(
                "Service Type",
                ["Wash Only (₹99)", "Wash + Dry (₹149)", "Ironing Only (₹19)"]
            )
            weight = st.slider("Estimated load weight (kg)", 2.0, 8.0, 5.0, 0.5)
            time_slot = st.selectbox(
                "Preferred Time Slot",
                ["Anytime Today", "Morning (7–11 AM)", "Afternoon (12–4 PM)", "Evening (5–9 PM)"]
            )
            payment_mode = st.selectbox(
                "Payment Mode",
                ["UPI", "Debit Card", "Credit Card", "Cash (at kiosk)"]
            )

        notes = st.text_area("Any special notes? (e.g. 'separate whites', 'delicate fabric')")

        submitted = st.form_submit_button("Confirm Booking ")

    if submitted:
        st.success(
            f"Thanks {name or 'there'}! Your request for **{service_type}** "
            f"({weight} kg, {time_slot}) has been recorded."
        )

        # 1) Show booking details
        booking_data = {
            "name": name,
            "phone": phone,
            "hostel": hostel,
            "room": room,
            "service_type": service_type,
            "weight": weight,
            "time_slot": time_slot,
            "payment_mode": payment_mode,
            "notes": notes,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        st.json(booking_data)

        # 2) Create a mock booking link (later you can replace with real backend URL)
        booking_link = (
            f"https://washhubb.example/booking?"
            f"phone={phone}&time={booking_data['timestamp']}"
        )

        # 3) Generate QR code for the booking link
        qr_img = qrcode.make(booking_link)
        buf = io.BytesIO()
        qr_img.save(buf, format="PNG")
        buf.seek(0)

        # 4) Show QR code and link
        st.subheader("Scan this QR to view your booking")
        st.image(buf, caption="Scan with your phone camera", use_container_width=False)

        st.write("Or open this link directly:")
        st.markdown(f"[🔗 Open booking link]({booking_link})")

# ABOUT & CONTACT
elif page == "About & Contact":
    st.header("About WashHubb ")

    st.markdown(
        "WashHubb is a **tech-enabled laundry solution** for students and high-density "
        "properties like hostels and PGs.\n\n"
        "We set up on-site smart machines with QR-based payments, affordable pricing, "
        "and flexible subscription packs so students never have to worry about laundry again."
    )

    st.subheader("Contact")
    st.markdown(
        " Jaipur, Rajasthan  \n"
        " support@washhubb.com  \n"
        " +91-98765-43210"
    )

# ----------------- FOOTER -----------------
st.markdown(
    f'<div class="footer">© {datetime.now().year} WashHubb Smart Laundry · Built with Streamlit</div>',
    unsafe_allow_html=True
)
