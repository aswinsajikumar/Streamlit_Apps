import streamlit as st

st.title("📝 Word Counter")

text = st.text_area("Enter text")

if text:
    words = text.split()
    characters = len(text)
    sentences = text.count(".") + text.count("!") + text.count("?")

    st.write("Words:", len(words))
    st.write("Characters:", characters)
    st.write("Sentences:", sentences)