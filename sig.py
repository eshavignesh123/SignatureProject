import streamlit as st

import cv2 

st.title("Signature Modification")


file_name = st.file_uploader("Upload file", type=["csv", "png", "jpg"])
  

