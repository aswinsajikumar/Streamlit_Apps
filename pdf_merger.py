import streamlit as st
from PyPDF2 import PdfMerger
from io import BytesIO

st.title("📄 PDF Merger")

uploaded_files = st.file_uploader(
    "Upload PDF files",
    type=["pdf"],
    accept_multiple_files=True
)

if uploaded_files:
    if st.button("Merge PDFs"):
        merger = PdfMerger()

        for pdf in uploaded_files:
            merger.append(pdf)

        output = BytesIO()
        merger.write(output)
        merger.close()

        st.success("PDFs merged successfully!")

        st.download_button(
            label="Download Merged PDF",
            data=output.getvalue(),
            file_name="merged.pdf",
            mime="application/pdf"
        )
