import streamlit as st
from database import add_order
from components.wallet_engine import deduct_wallet

def elder_home():
    st.header("Elder Mode")

    st.markdown("### What would you like to do?")

    if st.button("🍲 Order Food", use_container_width=True):

        item = "Home Style Meal - ₹150"
        price = 150

        new_balance = deduct_wallet(st.session_state.wallet, price)

        if new_balance is not None:
            st.session_state.wallet = new_balance
            add_order(st.session_state.user, item, price)
            st.success("Your food is on the way ❤️")
        else:
            st.error("Family Wallet Low Balance")

    if st.button("🔁 Repeat Last Order", use_container_width=True):
        st.success("Last order repeated!")