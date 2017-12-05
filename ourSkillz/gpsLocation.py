import sys
import os

print(sys.path)
print("\n\n\n")
#sys.path.insert(0, './dependencies/')
#print(sys.path)
#print "importing gps from" + __file__
#import gps

respond_to = ["where", "am", "I", "current", "location"]

def respond(array):
    count = 0
    for word in array:
        if word in respond_to:
            count = count + 1
    return count

def handle_input(string):
    loc = gps.getLocation()
    address = loc.getFormattedAddress(self)

    return "You are currently at " + loc.getLatitude() + "latitude, " \
            + loc.getLongitude() + "longitude with street address " \
            + loc.getFormattedAddress()
