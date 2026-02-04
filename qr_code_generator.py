import streamlit as st
import qrcode
from io import BytesIO

st.title("📱 QR Code Generator")

data = st.text_input("Enter text or URL")

if st.button("Generate QR Code"):
    if data:
        qr = qrcode.make(data)
        buffer = BytesIO()
        qr.save(buffer, format="PNG")
        st.image(buffer.getvalue())
    else:
        st.warning("Please enter some text or a URL")