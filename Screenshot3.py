import time
import subprocess
import os
from PIL import ImageGrab
# import urlparse

def get_current_status(netss):
    # netss = subprocess.check_output('ss -rt', shell=True)
    command = subprocess.getoutput("sudo ss -nt state established dst :443")
    print('command',command)
    if 'facebook' in netss:
        out_put = subprocess.check_output('import -window root "/home/user/test/new_$(date +%F-%N).png"', shell=True)
        time.sleep(3)
    elif 'youtube' in netss:
        out_put = subprocess.check_output('import -window root “/home/user/test/new_$(date +%F-%N).png”', shell=True)
    else:
        print('Not yet time to capture')

def main():
    im1 = ImageGrab.grab(bbox= None)
    im1.show()
# while True:
main()
    # time.sleep(10)