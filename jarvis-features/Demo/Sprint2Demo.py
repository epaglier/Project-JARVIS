#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 13:04:03 2017

@author: Evan
"""
import os

print("Evans Demo Section:\n")

raw_input("Story 34 (GPS AI):\n\nFirst lets take a look at the Data\nPress enter to continue...\n")

import clustering

with open("output.txt", 'r') as fin:
    print fin.read()

fin.close()

raw_input("This is a sample of the data returned from our database by download.py.\n\nPress enter to run AI.\n(Average time to run on Pi ~30 min, Mac ~2 min.)\n")

cluster.findAndPlot()

if raw_input("This is a graphical representation of the points and a list of the points ordered by rank (number of close neighbors).\n\nNow we can either demo the once a day function or just show its source code.\nThis will just print when it would run in debug mode.\nType y or n to continue...\n") == 'y':
    import RunOnceADay
else:
    print "Here is the code used to make this happen..\n----------"
    with open("RunOnceADay.py", 'r') as fin:
        print fin.read() 
    fin.close()
    print "----------\n"
    
print 'Otherwise use the method to invoke early.'

raw_input("Story 5 (Say cheese!):\n\nLets start with the most basic function, taking a picture.\nPress enter and say cheese!\n")

import Take_picture as cam
cam.takePicture()
print ("Lets take a look at our dedicated folder \"Image folder\"\n")
print os.listdir("./Image folder/")