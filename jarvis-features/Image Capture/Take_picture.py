#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 17:40:11 2017

@author: Evan
"""

import os
import time
import cv2

camera_port = 0
camera = None
num = 0

def takePicture():    
    #Shutter images
    global camera
    print("Taking image, hold stil....")
    camera = cv2.VideoCapture(camera_port)
    ramp_frames = 30
    for i in xrange(ramp_frames):
     temp = get_image()
     
    #Actually take it
    camera_capture = get_image()
    camera.release()
    file = "./Image folder/" + raw_input("Name your file! (without extention)\n") + ".png"
    cv2.imwrite(file, camera_capture)


def get_image():
    global camera
    retval, im = camera.read()
    return im

def leave():
    global camera
    camera.release
import atexit
atexit.register(leave)