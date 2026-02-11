import streamlit as st
from datetime import date

st.title("🎂 Age Calculator")

dob = st.date_input("Select your date of birth")

if dob:
    today = date.today()

    years = today.year - dob.year
    months = (today.year - dob.year) * 12 + today.month - dob.month
    days = (today - dob).days

    # Adjust if birthday hasn't occurred yet this year
    if (today.month, today.day) < (dob.month, dob.day):
        years -= 1

    st.subheader("Your Age")
    st.write("Years:", years)
    st.write("Months:", months)
    st.write("Days:", days)
