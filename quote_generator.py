import streamlit as st
import random

st.title('💬 Quote Generator')

quotes = [
    "Believe in yourself.",
    "Consistency beats talent.",
    "Small steps every day.",
    "Focus on progress, not perfection.",
    "Discipline creates freedom."
]

if st.button('Get a Quote'):
    quote = random.choice(quotes)
    st.subheader(quote)
    