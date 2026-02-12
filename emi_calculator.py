import streamlit as st

st.title("🏦 Loan EMI Calculator")

principal = st.number_input("Loan Amount", min_value=0.0, step=1000.0)
rate = st.number_input("Annual Interest Rate (%)", min_value=0.0, step=0.1)
years = st.number_input("Loan Duration (Years)", min_value=1, step=1)

if st.button("Calculate EMI"):
    monthly_rate = rate / 100 / 12
    months = years * 12

    if monthly_rate > 0:
        emi = (principal * monthly_rate * (1 + monthly_rate) ** months) / ((1 + monthly_rate) ** months - 1)
    else:
        emi = principal / months

    total_payment = emi * months
    total_interest = total_payment - principal

    st.subheader("Results")
    st.write(f"Monthly EMI: {emi:.2f}")
    st.write(f"Total Payment: {total_payment:.2f}")
    st.write(f"Total Interest: {total_interest:.2f}")
