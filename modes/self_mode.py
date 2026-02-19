import streamlit as st
from database import add_order
from components.wallet_engine import deduct_wallet

def self_home():
    st.header("Self Ordering Mode")

    restaurant = st.selectbox("Select Restaurant", ["Pizza Hub", "Healthy Bowl", "South Meals"])

    item = st.selectbox("Select Item", [
        "Veg Pizza - ₹250",
        "Salad Bowl - ₹180",
        "South Thali - ₹200"
    ])

    price = int(item.split("₹")[1])

    if st.button("Place Order"):
        new_balance = deduct_wallet(st.session_state.wallet, price)

        if new_balance is not None:
            st.session_state.wallet = new_balance
            add_order(st.session_state.user, item, price)
            st.success("Order Placed!")
        else:
            st.error("Insufficient Wallet Balance")
