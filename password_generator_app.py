import streamlit as st
import random
import string

st.title("🔐 Password Generator")

length = st.slider("Password length", min_value=6, max_value=32, value=12)

use_letters = st.checkbox("Include letters", value=True)
use_numbers = st.checkbox("Include numbers")
use_symbols = st.checkbox("Include symbols")

if st.button("Generate Password"):
    chars = ""

    if use_letters:
        chars += string.ascii_letters
    if use_numbers:
        chars += string.digits
    if use_symbols:
        chars += "!@#$%^&*"

    if chars:
        password = "".join(random.choice(chars) for _ in range(length))
        st.subheader("Generated Password")
        st.code(password)
    else:
        st.warning("Please select at least one character type.")
