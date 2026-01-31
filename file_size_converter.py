import streamlit as st

st.title("📦 File Size Converter")

value = st.number_input("Enter file size", min_value=0.0)

from_unit = st.selectbox("From", ["Bytes", "KB", "MB", "GB"])
to_unit = st.selectbox("To", ["Bytes", "KB", "MB", "GB"])

units = {
    "Bytes": 1,
    "KB": 1024,
    "MB": 1024 ** 2,
    "GB": 1024 ** 3
}

if st.button("Convert"):
    bytes_value = value * units[from_unit]
    result = bytes_value / units[to_unit]
    st.subheader(f"Result: {result:.2f} {to_unit}")