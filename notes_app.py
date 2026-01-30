import streamlit as st

st.title("🗒️ Notes App")

if "notes" not in st.session_state:
    st.session_state.notes = []

note = st.text_area("Write a note")

if st.button("Save Note"):
    if note:
        st.session_state.notes.append(note)
        st.success("Note saved")

st.subheader("Saved Notes")

for i, n in enumerate(st.session_state.notes, start=1):
    st.write(f"{i}. {n}")