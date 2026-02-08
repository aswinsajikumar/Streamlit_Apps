import streamlit as st

st.title("📝 Markdown Previewer")

markdown_text = st.text_area(
    "Write Markdown here",
    height=300,
    placeholder="# Heading\n\n**Bold text**\n\n- List item"
)

st.subheader("Preview")

if markdown_text:
    st.markdown(markdown_text)
else:
    st.info("Start typing Markdown to see the preview")
