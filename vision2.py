# Import required packages
import cv2
import pytesseract
from pytesseract import Output

# Mention the installed location of Tesseract-OCR in your system
pytesseract.pytesseract.tesseract_cmd = r"/usr/local/bin/tesseract/"

# Read image from which text needs to be extracted
img = cv2.imread("./seamless1.png")
cv2.imshow('',img)
cv2.waitKey()
rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
cv2.imshow('',rgb)
cv2.waitKey()

results = pytesseract.image_to_data(rgb,lang='eng',output_type=Output.DICT)
print(results)