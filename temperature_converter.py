import streamlit as st

st.title("🌡️ Temperature Converter")

value = st.number_input("Enter temperature value")

from_unit = st.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin"])
to_unit = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"])

if st.button("Convert"):
    if from_unit == to_unit:
        result = value
    elif from_unit == "Celsius" and to_unit == "Fahrenheit":
        result = (value * 9/5) + 32
    elif from_unit == "Celsius" and to_unit == "Kelvin":
        result = value + 273.15
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        result = (value - 32) * 5/9
    elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
        result = (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin" and to_unit == "Celsius":
        result = value - 273.15
    else:  # Kelvin to Fahrenheit
        result = (value - 273.15) * 9/5 + 32

    st.subheader(f"Result: {result:.2f}")
