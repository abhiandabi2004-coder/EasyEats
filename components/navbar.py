import streamlit as st

def show_navbar():
    st.sidebar.title("Navigation")

    if st.sidebar.button("Logout"):
        st.session_state.clear()
        st.rerun()
