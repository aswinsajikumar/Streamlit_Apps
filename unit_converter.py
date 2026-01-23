import streamlit as st

st.title("🔄 Unit Converter")

value = st.number_input("Enter value", min_value=0.0)

unit_type = st.selectbox(
    "Select conversion type",
    ["Length", "Weight"]
)

if unit_type == "Length":
    option = st.selectbox(
        "Convert",
        [
            "Meters to Kilometers",
            "Kilometers to Meters",
            "Meters to Millimeters",
            "Millimeters to Meters",
            "Kilometers to Miles",
            "Miles to Kilometers"
        ]
    )

    if option == "Meters to Kilometers":
        result = value / 1000
    elif option == "Kilometers to Meters":
        result = value * 1000
    elif option == "Meters to Millimeters":
        result = value * 1000
    elif option == "Millimeters to Meters":
        result = value / 1000
    elif option == "Kilometers to Miles":
        result = value * 0.621371
    else:  # Miles to Kilometers
        result = value / 0.621371

elif unit_type == "Weight":
    option = st.selectbox(
        "Convert",
        ["Kilograms to Grams", "Grams to Kilograms"]
    )

    if option == "Kilograms to Grams":
        result = value * 1000
    else:
        result = value / 1000

if st.button("Convert"):
    st.subheader(f"Result: {result}")