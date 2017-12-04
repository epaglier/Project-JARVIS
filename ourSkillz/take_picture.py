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

respond_to = ["take","picture"]

def respond(array):
    count = 0
    for word in array:
        if word in respond_to:
            count = count + 1
    return count

def handle_input(string):
    try:
        takePicture()
        return "Done!"
    except:
        return "Sorry I couldn't for some reason"

def takePicture():    
    #Shutter images
    global camera
    print("Taking image, hold still....")
    camera = cv2.VideoCapture(camera_port)
    ramp_frames = 30
    for i in xrange(ramp_frames):
        temp = get_image()
                                          
    #Actually take it
    camera_capture = get_image()
    camera.release()
    file = "./Image_folder/" + "Demo.jpg"#raw_input("Name your file! (without extention)\n") + ".png"
    cv2.imwrite(file, camera_capture)


def get_image():
    global camera
    retval, im = camera.read()
    return im

def leave():
    global camera
    camera.release
