import streamlit as st

st.title("🛒 Unit Price Calculator")

st.subheader("Product A")
price_a = st.number_input("Price of Product A", min_value=0.0)
qty_a = st.number_input("Quantity of Product A", min_value=0.01)

st.subheader("Product B")
price_b = st.number_input("Price of Product B", min_value=0.0)
qty_b = st.number_input("Quantity of Product B", min_value=0.01)

if st.button("Compare"):
    unit_a = price_a / qty_a
    unit_b = price_b / qty_b

    st.write(f"Product A price per unit: {unit_a:.2f}")
    st.write(f"Product B price per unit: {unit_b:.2f}")

    if unit_a < unit_b:
        st.success("Product A is cheaper per unit ✅")
    elif unit_b < unit_a:
        st.success("Product B is cheaper per unit ✅")
    else:
        st.info("Both products cost the same per unit")