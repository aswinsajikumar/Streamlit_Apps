import streamlit as st
import time

st.title("⏳ Pomodoro Timer")

if "running" not in st.session_state:
    st.session_state.running = False

if st.button("Start 25 Minute Timer"):
    st.session_state.running = True

if st.session_state.running:
    placeholder = st.empty()
    seconds = 25 * 60

    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        placeholder.subheader(f"{mins:02d}:{secs:02d}")
        time.sleep(1)
        seconds -= 1

    st.success("Time's up! Take a break 🎉")
    st.session_state.running = False
