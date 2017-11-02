import gps
import urllib2
import json
import os
import sys

user = os.getlogin()
sys.path.insert(0, '../weather')

import weather

# Test file

response = urllib2.urlopen("https://maps.googleapis.com/maps/api/geocode/json?latlng=40.43201666666666,-86.92631166666666&key=AIzaSyBMK5WI2yWUnBpnToA7FX0bKf8Lkb3RWBQ").read()
jsonthing = json.loads(response)

street_number = jsonthing['results'][0]['address_components'][0]['short_name']
street = jsonthing['results'][0]['address_components'][1]['short_name']

loc = gps.getLocation()
w = weather.getWeatherHere()

print "Velocity: " + repr(loc.getVelocity())
print "Long: " + repr(loc.getLongitude())
print "Lat: " + repr(loc.getLatitude())
print "Fix: " + repr(loc.getFix())
print "Type: " + repr(loc.getTransportation())
print "---------------------------------"
print "Precipitation: " + w.getPrecipitation()
print "Temperature: %.2f F" % w.getTempF()
print "Humidity: " + repr(w.getHumidity()) + "%"
print "Wind speed: " + repr(w.getWind()) + " m/s"

print street_number + " " + street
