import streamlit as st
import re

st.title("🔐 Password Strength Checker")

password = st.text_input("Enter a password", type="password")

def check_strength(pwd):
    score = 0

    if len(pwd) >= 8:
        score += 1
    if re.search(r"[A-Z]", pwd):
        score += 1
    if re.search(r"[a-z]", pwd):
        score += 1
    if re.search(r"[0-9]", pwd):
        score += 1
    if re.search(r"[^A-Za-z0-9]", pwd):
        score += 1

    return score

if password:
    strength = check_strength(password)

    if strength <= 2:
        st.error("Weak password")
    elif strength <= 4:
        st.warning("Medium strength password")
    else:
        st.success("Strong password")
