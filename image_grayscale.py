import streamlit as st
from PIL import Image

st.title("🖼️ Image to Grayscale Converter")

uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)

    st.subheader("Original Image")
    st.image(image)

    grayscale = image.convert("L")

    st.subheader("Grayscale Image")
    st.image(grayscale)
