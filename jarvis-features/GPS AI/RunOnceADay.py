#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 14:18:14 2017

@author: Evan
"""

import makeDailySummary
import datetime
import time

demo = 0

print datetime.datetime.now()
currHour = int(str(datetime.datetime.now()).split(":")[0].split(" ")[1])
currMin = int(str(datetime.datetime.now()).split(":")[1])

time.sleep(1)

while 1:
    if int(str(datetime.datetime.now()).split(":")[0].split(" ")[1]) == currHour and int(str(datetime.datetime.now()).split(":")[1]) == currMin + 1 and not demo:
        makeDailySummary.make()
    elif int(str(datetime.datetime.now()).split(":")[0].split(" ")[1]) == currHour and int(str(datetime.datetime.now()).split(":")[1]) == currMin + 1 and demo:
        print "Would be clustering now..."
        break
    elif demo:
        print 'Waiting.'
