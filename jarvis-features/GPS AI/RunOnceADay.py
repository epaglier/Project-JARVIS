#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 14:18:14 2017

@author: Evan
"""

import clustering
import datetime

print datetime.datetime.now()

while 1:
    if int(str(datetime.datetime.now()).split(":")[0].split(" ")[1]) == 14 and int(str(datetime.datetime.now()).split(":")[1]) == 52:
        clustering.findAndPlot()