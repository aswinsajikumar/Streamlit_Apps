import streamlit as st

st.title('🔢 Simple Counter App')

if 'count' not in st.session_state:
    st.session_state.count = 0

col1, col2 = st.columns(2)

with col1:
    if st.button('➖ Decrease'):
        st.session_state.count -= 1
    
with col2:
    if st.button('➕ Increase'):
        st.session_state.count += 1
    

st.write('Current Count:', st.session_state.count)