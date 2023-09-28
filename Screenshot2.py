#!/usr/bin/env python3
import subprocess
import time
import pyscreenshot as ImageGrab
import os
if not 'DISPLAY' in os.environ:
    os.environ['DISPLAY'] = ":0"

class NewCapture:
    
    command = subprocess.getoutput("sudo ss -nt state established dst :443")
    file_name = time.strftime("%Y-%m-%d-%H-%M-%S" +".png")
    grab = ""
    def funct_capture(self):
        path = os.getcwd()
        print(self.command)
        if ":google.com" in self.command:

            self.grab = ImageGrab.grab_to_file(path +"/%s" % self.file_name)

        else:
            pass

firstcommand = NewCapture()
firstcommand.funct_capture()