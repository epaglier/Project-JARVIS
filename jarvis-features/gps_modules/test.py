import gps
import urllib2
import json

# Test file

response = urllib2.urlopen("https://maps.googleapis.com/maps/api/geocode/json?latlng=40.43201666666666,-86.92631166666666&key=AIzaSyBMK5WI2yWUnBpnToA7FX0bKf8Lkb3RWBQ").read()
jsonthing = json.loads(response)

street_number = repr(jsonthing['results'][0]['address_components'][0]['short_name'])[2:-1]
street = repr(jsonthing['results'][0]['address_components'][1]['short_name'])[2:-1]

loc = gps.getLocation()

print "Velocity: " + repr(loc.getVelocity())
print "Long: " + repr(loc.getLongitude())
print "Lat: " + repr(loc.getLatitude())
print "Fix: " + repr(loc.getFix())
print "Type: " + repr(loc.getTransportation())

print street_number + " " + street
