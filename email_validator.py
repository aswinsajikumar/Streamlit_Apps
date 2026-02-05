import streamlit as st
import re

st.title("📧 Email Validator")

email = st.text_input("Enter an email address")

pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

if email:
    if re.match(pattern, email):
        st.success("Valid email address")
    else:
        st.error("Invalid email address")
