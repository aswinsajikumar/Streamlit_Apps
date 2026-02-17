import streamlit as st
from PIL import Image
from io import BytesIO

st.title("🖼️ Image Resizer")

uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Original Image")

    width = st.number_input("New Width", min_value=1, value=image.width)
    height = st.number_input("New Height", min_value=1, value=image.height)

    if st.button("Resize Image"):
        resized_image = image.resize((width, height))

        st.image(resized_image, caption="Resized Image")

        buffer = BytesIO()
        resized_image.save(buffer, format="PNG")

        st.download_button(
            label="Download Resized Image",
            data=buffer.getvalue(),
            file_name="resized_image.png",
            mime="image/png"
        )
