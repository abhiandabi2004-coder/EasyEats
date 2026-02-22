import streamlit as st
from database import init_db
from auth import login
from modes.self_mode import self_home
from modes.parental_mode import parent_home
from modes.elder_mode import elder_home
from components.navbar import show_navbar
from config import DEFAULT_WALLET_BALANCE, DEFAULT_SPEND_LIMIT


# -----------------------------
# INITIALIZE DATABASE
# -----------------------------
init_db()

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Mindful Food Delivery",
    layout="wide"
)

# -----------------------------
# CUSTOM STYLING
# -----------------------------
st.markdown("""
<style>
.stButton>button {
    border-radius: 12px;
    background-color: #ff4b4b;
    color: white;
    font-weight: bold;
    padding: 8px 16px;
}

.sidebar .sidebar-content {
    background-color: #f8f9fa;
}

h1, h2, h3 {
    color: #333333;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# SESSION STATE INIT
# -----------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "wallet" not in st.session_state:
    st.session_state.wallet = DEFAULT_WALLET_BALANCE

if "limit" not in st.session_state:
    st.session_state.limit = DEFAULT_SPEND_LIMIT

if "cart" not in st.session_state:
    st.session_state.cart = []

# -----------------------------
# LOGIN FLOW
# -----------------------------
if not st.session_state.logged_in:
    login()

else:
    # Sidebar
    show_navbar()

    st.sidebar.markdown("### 👤 User Info")
    st.sidebar.write(f"Name: {st.session_state.user}")
    st.sidebar.write(f"💰 Wallet: ₹ {st.session_state.wallet}")
    st.sidebar.write(f"📊 Spend Limit: ₹ {st.session_state.limit}")

    st.sidebar.markdown("---")

    # Mode Selection
    st.title("🍲 Mindful Food Delivery")
    st.subheader("Choose Your Mode")

    mode = st.selectbox(
        "Select Mode",
        ["Self Ordering", "Parental Mode", "Elder Mode"]
    )

    st.markdown("---")

    # -----------------------------
    # ROUTING TO MODES
    # -----------------------------
    if mode == "Self Ordering":
        self_home()

    elif mode == "Parental Mode":
        parent_home()

    elif mode == "Elder Mode":
        elder_home()
