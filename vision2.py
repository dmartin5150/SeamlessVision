# Import required packages
import cv2
import pytesseract
from pytesseract import Output
from PIL import ImageGrab, Image
import time
import os
import pyautogui
from flask import Flask, flash, request, redirect, render_template, send_from_directory,abort
from flask_cors import CORS
import threading
import json
import numpy as np

app = Flask(__name__)
CORS(app)
app.secret_key = "seamless care" # for encrypting the session
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024



# Mention the installed location of Tesseract-OCR in your system
pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

def convertImage(img):
# Read image from which text needs to be extracted
    pic_array = np.array(img)
    converted = cv2.cvtColor(pic_array,cv2.COLOR_BGRA2GRAY)
    convertedImage = Image.fromarray(converted)
    convertedImage.show()
    return converted


def getImageData(img):
    return pytesseract.image_to_data(img,lang='eng',output_type=Output.DICT)




def getMRNandFIN(img,imgData):
    curData = imgData['text']
    curMRN = ''
    curFIN = ''
    if (len(curData) > 0):
        for i in range(0, len(curData)):
            curElement = curData[i]
            if ('MRN:' in curElement):
                print('mrn index', i)
                print('mrn', curElement)
                parsedElement = curElement.split(":")
                curMRN = parsedElement[1]
            if ('Fin#:' in curElement):
                print('found fin')
                parsedElement = curElement.split(":")
                curFIN = parsedElement[1]
    return curMRN, curFIN


        





def getScreenshot():
    # img = os.system("screencapture screen.png")
    # img = ImageGrab.grab(bbox= None,include_layered_windows=True, all_screens=True)
    img = ""
    img = pyautogui.screenshot()
    # img.show()
    return img


# def getData():
#         print('getting screenshot')
#         img = getScreenshot()
#         # img.show()
#         img = convertImage(img)
#         # img.show()
#         print('getting data')
#         imgData = getImageData(img)
#         # img.show()
#         print(imgData['text'])
#         print('getting MRN')
#         getMRNandFIN(img,imgData)
        # print('curmrn', curMRN,'curfin', curFIN)

# getData()

@app.route('/patientData', methods=['GET'])
def get_patient_data_async():
    print('getting screenshot')
    img = getScreenshot()
    # img.show()
    print('getting data')
    # img = convertImage(img)
    imgData = getImageData(img)
    # img.show()
    print(imgData['text'])
    print('getting MRN')
    curMRN, curFIN = getMRNandFIN(img,imgData)
    print('curmrn', curMRN,'curfin', curFIN)
    return json.dumps({'FIN':curFIN,'MRN':curMRN}), 20

app.run(host='0.0.0.0', port=5001)

    
