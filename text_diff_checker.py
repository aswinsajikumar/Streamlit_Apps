import streamlit as st
import difflib

st.title("🔍 Text Difference Checker")

text1 = st.text_area("Text A", height=200)
text2 = st.text_area("Text B", height=200)

if st.button("Compare"):
    if text1 and text2:
        diff = difflib.ndiff(text1.splitlines(), text2.splitlines())

        st.subheader("Differences")
        for line in diff:
            if line.startswith("+ "):
                st.success(line)
            elif line.startswith("- "):
                st.error(line)
            elif line.startswith("? "):
                continue
            else:
                st.write(line)
    else:
        st.warning("Please enter both texts")
