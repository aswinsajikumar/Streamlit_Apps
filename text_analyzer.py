import streamlit as st

st.title("📝 Text Analyzer")

text = st.text_area("Enter your text below:")

analyze = st.button("🔍 Analyze Text")

if analyze:
    if text.strip():
        char_count = len(text)
        word_count = len(text.split())
        line_count = len(text.splitlines())

        st.subheader("📊 Analysis Results")
        st.markdown(f"#### Characters: **{char_count}**")
        st.markdown(f"#### Words: **{word_count}**")
        st.markdown(f"#### Lines: **{line_count}**")
    else:
        st.warning("Please enter some text before analyzing.")
