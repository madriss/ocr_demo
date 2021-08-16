import cv2
import numpy as np
from PIL import Image
import pytesseract
import re
pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract" #  to set to your own tesseract installation folder

# To do utiliser use NER for detecting fields of interest

def get_iban_from_txt(txt):
    pattern = "FR[a-zA-Z0-9]{2}\s?([0-9]{4}\s?){2}([0-9]{2})([a-zA-Z0-9]{2}\s?)([a-zA-Z0-9]{4}\s?){2}([a-zA-Z0-9]{1})([0-9]{2})\s?"
    result = re.search(pattern, txt)
    return result


def correct_rotation(img):
    """This functions corrects for eventual text orientation issues"""
    newdata = pytesseract.image_to_osd(img)
    angle = int(re.search('(?<=Rotate: )\d+', newdata).group(0))
    angle= 360 - angle
    (h, w) = img.shape[:2]
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(img, M, (w, h))
    return rotated


def ocr_img(img, lang="fra"):
    text = pytesseract.image_to_string(img, lang=lang)
    return "".join(text.replace(" ", "").split("\n"))
