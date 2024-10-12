import streamlit as st
from PIL import Image as Img
with st.expander("Start camera."):
    cam_image = st.camera_input("Camera")
if cam_image:
    image = Img.open(cam_image)
    gray_img = image.convert("L")
    st.image(gray_img)