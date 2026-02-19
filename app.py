import streamlit as st
from database import init_db
from auth import login
from components.navbar import show_navbar
from modes.self_mode import self_home
from modes.parental_mode import parent_home
from modes.elder_mode import elder_home
from config import DEFAULT_WALLET_BALANCE, DEFAULT_SPEND_LIMIT

init_db()

st.set_page_config(page_title="Mindful Food Delivery", layout="wide")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "wallet" not in st.session_state:
    st.session_state.wallet = DEFAULT_WALLET_BALANCE

if "limit" not in st.session_state:
    st.session_state.limit = DEFAULT_SPEND_LIMIT

if not st.session_state.logged_in:
    login()
else:
    show_navbar()

    st.sidebar.write(f"👤 User: {st.session_state.user}")
    st.sidebar.write(f"💰 Wallet: ₹{st.session_state.wallet}")

    st.title("Select Mode")

    mode = st.selectbox("Choose Mode", ["Self Ordering", "Parental Mode", "Elder Mode"])

    if mode == "Self Ordering":
        self_home()

    elif mode == "Parental Mode":
        parent_home()

    elif mode == "Elder Mode":
        elder_home()