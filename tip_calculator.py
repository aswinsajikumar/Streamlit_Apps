import streamlit as st

st.header('💵Tip Calculator')

bill = st.number_input('Enter bill amount: ', min_value=0.0, format='%.2f', step=5.0)
tip_percent = st.slider('Select tip percentage',0, 30, 5)

if st.button('Calculate'):
    tip = bill * (tip_percent/100)
    total = bill + tip

    st.subheader(f'Tip: ${tip}')
    st.subheader(f'Total: ${total}')