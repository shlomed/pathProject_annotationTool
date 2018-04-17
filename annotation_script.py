
# coding: utf-8


import os
from glob import glob
import cv2
from pprint import pprint
import subprocess
import webbrowser
import argparse
import time


import threading

import sys
sys.path.insert(0, 'tools/image-labelling-tool/')

from flask_app_mod import run_annotation_tool

import warnings
warnings.simplefilter("ignore")

path  = "data/"

image_dirs = os.listdir(path)

for i, img_dir in enumerate(image_dirs):
    files = os.listdir(path + '/' + img_dir)
    mystr = ""
    if len([f for f in files if f.endswith(".json")])>0:
        mystr = " (Done)"
    print ('{}. {}'.format(i, img_dir)+mystr)
choose_index = raw_input('chooose file number:')
image_dir = path + image_dirs[int(choose_index)] + "/"
# print(image_dir)

def run_cmd_command(command):
    proc = subprocess.Popen('cmd.exe', stdin = subprocess.PIPE, stdout = subprocess.PIPE)
    stdout, stderr = proc.communicate(command)
    return stdout, stderr


path_to_flask_app = "tools/image-labelling-tool/"
labels_path = "configurtion_files/labeling_tool/labels.yml"

def target():
    print("starting")
    run_annotation_tool(image_dir, labels_path)
    print("exiting")

t1 = threading.Thread(name="flask_app_%d"%1, target=target)

t1.start()


time.sleep(10)
webbrowser.open_new_tab("http://localhost:5000")
print("opening browser tab with the annotation tool")
