# import pyautogui
# import os
# import requests
# from flask import request
# from splinter import browser


# path = os.getcwd()
# myScreenshot= pyautogui.screenshot()
# print(browser.url)
# print(request.host.split(':')[0])
# myScreenshot.save(path + '/myscreenshot.png')

from pywinauto.application import Application # pip install pywinauto

app = Application(backend='uia')

app.connect(title_re=".*Chrome.*")

element_name="Address and search bar"

dlg = app.top_window()

url = dlg.child_window(title=element_name, control_type="Edit").get_value()

print(url)