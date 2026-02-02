import streamlit as st
import random
import string

st.title("👤 Username Generator")

length = st.slider("Username length", 5, 15, 8)
use_numbers = st.checkbox("Include numbers")
use_underscore = st.checkbox("Include underscore")

characters = string.ascii_lowercase

if use_numbers:
    characters += string.digits
if use_underscore:
    characters += "_"

if st.button("Generate Username"):
    username = "".join(random.choice(characters) for _ in range(length))
    st.subheader("Generated Username")
    st.code(username)