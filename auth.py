import streamlit as st

def login():
    st.subheader("Login")

    name = st.text_input("Enter Your Name")

    if st.button("Continue"):
        if name:
            st.session_state.user = name
            st.session_state.logged_in = True