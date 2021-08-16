import numpy as np 
import pandas as pd 
import pytesseract
from PIL import Image
from io import StringIO
from utils import get_iban_from_txt, ocr_img
import os
import joblib
import time
import streamlit as st

st.set_option('deprecation.showPyplotGlobalUse', False)

st.title('IBAN Extraction System - Madriss Seksaoui')
st.write("Attention : cet outil a un but strictement démonstratif et ne doit pas être utilisé dans des conditions réelles")


uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # Can be used wherever a "file-like" object is accepted:
    req_time = time.time()
    img = Image.open(uploaded_file)
    read_time = time.time() - req_time
    st.write("image fournie : ")
    st.image(img)
    start_time = time.time()
    text = ocr_img(img)
    ocr_time = time.time() - start_time
    iban = get_iban_from_txt(text)
    if iban is not None:
        iban = iban.group()
        st.write("IBAN trouvé")
        st.write(iban)
    else:
        st.write("Aucun IBAN trouvé")
    with open("logs/times.txt", "a") as file:
        file.write(f"{req_time}, {read_time}, {ocr_time}, {iban}\n")