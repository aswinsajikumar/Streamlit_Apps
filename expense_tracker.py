import streamlit as st

st.title("💸 Expense Tracker")

if "expenses" not in st.session_state:
    st.session_state.expenses = []

name = st.text_input("Expense name")
amount = st.number_input("Amount", min_value=0.0, format="%.2f")

if st.button("Add Expense"):
    if name and amount > 0:
        st.session_state.expenses.append({"name": name, "amount": amount})
        st.success("Expense added")
    else:
        st.warning("Please enter a valid name and amount")

if st.session_state.expenses:
    st.subheader("Expenses")

    total = 0
    for expense in st.session_state.expenses:
        st.write(f"{expense['name']} - ${expense['amount']}")
        total += expense["amount"]

    st.subheader(f"Total: ${total:.2f}")