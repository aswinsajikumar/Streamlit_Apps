import streamlit as st

st.title("🧾 Simple Invoice Generator")

client = st.text_input("Client Name")
item = st.text_input("Item Name")
quantity = st.number_input("Quantity", min_value=1, step=1)
price = st.number_input("Price per Item", min_value=0.0, step=1.0)

if st.button("Generate Invoice"):
    total = quantity * price

    st.subheader("Invoice Summary")
    st.write("Client:", client)
    st.write("Item:", item)
    st.write("Quantity:", quantity)
    st.write("Price per Item:", price)
    st.write(f"Total Amount: {total:.2f}")
