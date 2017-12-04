import sys
import os
import gps
import datetime
import mysql.connector
import time
import RPi.GPIO as GPIO

track = 1

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)

def endLightCycle():
    GPIO.output(21, 0)
    GPIO.cleanup()

def stopTracking():
    track = 0

def startTracking():
    track = 1

mode = 1
timeToWait = 0
cnx = mysql.connector.connect(user='pi', password='sudo', database='test')
cursor = cnx.cursor()
try:
    while True:
         if track:
             GPIO.output(21, mode)
             if mode:
                  mode = 0
             else:
                  mode = 1
             time.sleep(timeToWait)
             GPIO.output(21, GPIO.LOW)
             stringToSend = ("INSERT INTO gps (time, latitude, longitude, velocity) VALUES (%s, %s, %s, %s)")
             loc = gps.getLocation()
             if loc.getFix():
                  latitude = str(loc.getLatitude())
                  print latitude
                  longitude = str(loc.getLongitude())
                  print longitude
                  velocity = str(loc.getVelocity())
                  print velocity
                  if (float(velocity) < 1.2) and (float(velocity) > -1.2):
                       timeToWait = 5
                  elif (float(velocity) > 11) or (float(velocity) < -11):
                       timeToWait = 0
                  else:
                       timeToWait = 1
                  print timeToWait
                  data= (datetime.datetime.now(), latitude, longitude, velocity)
                  cursor.execute(stringToSend, data)
                  cnx.commit()
                  print "uploaded"
             else:
                  print "No satelite fix"
except KeyboardInterrupt:
    endLightCycle()
    try:
         sys.exit(0)
    except SystemExit:
         os._exit(0)

import atexit
atexit.register(endLightCycle)
