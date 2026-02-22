import streamlit as st
import time

st.title("⌨️ Typing Speed Test")

sample_text = "Streamlit makes it easy to build interactive web apps using Python."

st.subheader("Type this sentence:")
st.write(sample_text)

if "start_time" not in st.session_state:
    st.session_state.start_time = None

user_input = st.text_area("Start typing here...")

if user_input and st.session_state.start_time is None:
    st.session_state.start_time = time.time()

if st.button("Calculate Result"):
    if user_input:
        end_time = time.time()
        time_taken = end_time - st.session_state.start_time

        words_typed = len(user_input.split())
        wpm = (words_typed / time_taken) * 60

        correct_chars = sum(1 for a, b in zip(user_input, sample_text) if a == b)
        accuracy = (correct_chars / len(sample_text)) * 100

        st.subheader("Results")
        st.write(f"Time Taken: {time_taken:.2f} seconds")
        st.write(f"Words Per Minute: {wpm:.2f}")
        st.write(f"Accuracy: {accuracy:.2f}%")

        st.session_state.start_time = None