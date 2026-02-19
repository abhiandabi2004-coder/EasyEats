import streamlit as st
import time

def simulate_tracking():
    st.subheader("Live Order Tracking")

    progress = st.progress(0)

    for i in range(100):
        time.sleep(0.02)
        progress.progress(i+1)

    st.success("Order Delivered Successfully!")