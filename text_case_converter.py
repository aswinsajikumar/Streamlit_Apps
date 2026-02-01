import streamlit as st

st.title("🔤 Text Case Converter")

text = st.text_area("Enter text")

if text:
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("UPPERCASE"):
            st.write(text.upper())

    with col2:
        if st.button("lowercase"):
            st.write(text.lower())

    with col3:
        if st.button("Title Case"):
            st.write(text.title())
