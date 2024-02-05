import streamlit as st

import cv2 
  
file_name = "signature.jpg"

src = cv2.imread(file_name, 1) 

tmp = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY) 
  
alpha = cv2.threshold(tmp, 100, 255, cv2.THRESH_BINARY_INV) 

b, g, r = cv2.split(src) 

rgba = [b, g, r, alpha] 

dst = cv2.merge(rgba, 4) 

cv2.imwrite("signature_white.png", dst) 


st.title("Signature Modification")
st.image("signature_white.png")

