# Import required packages
import cv2
import pytesseract
from pytesseract import Output
from PIL import ImageGrab
import time
import os
import pyautogui
from flask import Flask, flash, request, redirect, render_template, send_from_directory,abort
from flask_cors import CORS
import threading
import json

app = Flask(__name__)
CORS(app)
app.secret_key = "seamless care" # for encrypting the session
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024



# Mention the installed location of Tesseract-OCR in your system
pytesseract.pytesseract.tesseract_cmd = r"/usr/local/bin/tesseract/"
curMRN = ''
curFIN = ''

def getImage(img):
# Read image from which text needs to be extracted

    return cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

def getImageData(img):
    return pytesseract.image_to_data(img,lang='eng',output_type=Output.DICT)



def getMRNandFIN(imgData):
    curData = imgData['text']
    global curMRN
    global curFIN
    if (len(curData) > 0):
        for i in range(0, len(curData)):
            curElement = curData[i]
            # if ('FIN' in curElement):
            #     print('found fin', curElement)
            if ('MRN:' in curElement):
                print('mrn index', i)
                print('mrn', curElement)
                curMRN = curElement
            if ('Fin#:' in curElement):
                print('found fin')
                curFIN = curElement
                print('fin', curElement)

        





def getScreenshot():
    # img = os.system("screencapture screen.png")
    # img = ImageGrab.grab(bbox= None,include_layered_windows=True, all_screens=True)
    img = ""
    img = pyautogui.screenshot()
    # img.show()
    return img


def getData():
    global curMRN, curFIN
    while True:
        print('getting screenshot')
        img = getScreenshot()
        print('getting data')
        imgData = getImageData(img)
        # img.show()
        print(imgData['text'])
        print('getting MRN')
        getMRNandFIN(imgData)
        print('curmrn', curMRN,'curfin', curFIN)

threading.Thread(target=getData).start()

@app.route('/patientData', methods=['POST'])
def get_patient_data_async():
    return json.dumps({'FIN':curFIN,'MRN':curMRN}), 20

app.run(host='0.0.0.0', port=5001)

    
