import gps
import urllib2
import json
import os
import sys

user = os.getlogin()
sys.path.insert(0, '../weather')

import weather

# Test file

loc = gps.getLocation()
w = weather.getWeatherHere()

print "Velocity: " + repr(loc.getVelocity())
print "Long: " + repr(loc.getLongitude())
print "Lat: " + repr(loc.getLatitude())
print "Fix: " + repr(loc.getFix())
print "Type: " + repr(loc.getTransportation())
print "Formatted Address: " + loc.getFormattedAddress()
print "Distance to Chicago (Driving): " + repr(loc.getDistTo("Chicago","driving")) + " km"
print "---------------------------------"
print "Directions to Chicago (Driving): " + loc.getDirectionsTo("Chicago","driving")
print "---------------------------------"
print "Precipitation: " + w.getPrecipitation()
print "Temperature: %.2f F" % w.getTempF()
print "Humidity: " + repr(w.getHumidity()) + "%"
print "Wind speed: " + repr(w.getWind()) + " m/s"

