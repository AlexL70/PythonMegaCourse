import streamlit as st
from PIL import Image as Img

uploaded_image = st.file_uploader("Upload image.")
with st.expander("Start camera."):
    cam_image = st.camera_input("Camera")
if cam_image or uploaded_image:
    if cam_image:
        image = Img.open(cam_image)
    else:
        image = Img.open(uploaded_image)
        print(uploaded_image)
    gray_img = image.convert("L")
    st.image(gray_img)