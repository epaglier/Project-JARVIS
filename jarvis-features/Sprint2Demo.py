#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 13:04:03 2017

@author: Evan
"""
import os

raw_input("Evans Demo Section:\nPress enter to continue...\n")


os.chdir("GPS AI/")

raw_input("Demoing GPS AI with debug prints.\nTime to run on Pi ~30 min, Mac ~2 min.\nPress enter to continue...\n")

import clustering as cluster

with open("output.txt", 'r') as fin:
    print fin.read()

fin.close()

raw_input("This is test data used...\nPress enter to continue...\n")

cluster.findAndPlot()

raw_input("Evan manual demo of once a day file:\nPress enter to continue...\n")

with open("RunOnceADay.py", 'r') as fin:
    print fin.read()

fin.close()
    
os.chdir("..")