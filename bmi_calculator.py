import streamlit as st

st.title("⚖️ BMI Calculator")

height = st.number_input("Enter your height (in meters)", min_value=0.5, max_value=2.5, step=0.01)
weight = st.number_input("Enter your weight (in kg)", min_value=10.0, max_value=300.0, step=0.5)

if st.button("Calculate BMI"):
    if height > 0 and weight > 0:
        bmi = weight / (height ** 2)

        st.subheader(f"Your BMI is: {bmi:.2f}")

        if bmi < 18.5:
            st.info("Category: Underweight")
        elif bmi < 25:
            st.success("Category: Normal weight")
        elif bmi < 30:
            st.warning("Category: Overweight")
        else:
            st.error("Category: Obese")
    else:
        st.warning("Please enter valid height and weight.")
