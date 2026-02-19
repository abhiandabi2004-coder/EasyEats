import streamlit as st
from components.spend_engine import check_spend_limit
from components.wallet_engine import deduct_wallet
from database import add_order

def parent_home():
    st.header("Parental Mode")

    limit = st.number_input("Set Spend Limit", value=st.session_state.limit)

    item_price = st.number_input("Enter Order Amount", min_value=50)

    if st.button("Confirm Order"):
        if check_spend_limit(item_price, limit):

            new_balance = deduct_wallet(st.session_state.wallet, item_price)

            if new_balance is not None:
                st.session_state.wallet = new_balance
                add_order(st.session_state.user, "Parental Order", item_price)
                st.success("Order Within Limit & Placed!")
            else:
                st.error("Insufficient Wallet Balance")

        else:
            st.error("Spend Limit Exceeded!")
