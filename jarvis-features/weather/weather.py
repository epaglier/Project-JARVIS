import urllib2
import json
import os
import sys

user = os.getlogin()
sys.path.insert(0, '../gps_modules/')

import gps

# End of imports

OWM_API_KEY = "051d34ddcb7b5d61a0acd1811c5b1834"

class Weather:

    # Constructor
    def __init__(self, _longitude, _latitude):
        self.longitude = _longitude;
        self.latitude = _latitude;
        query = "http://api.openweathermap.org/data/2.5/weather?lat=" + repr(self.latitude) + "&lon=" + repr(self.longitude) + "&appid=" + OWM_API_KEY

        raw_weather_data = urllib2.urlopen(query).read()
        parsed_data = json.loads(raw_weather_data)
        self.temp_kelvin = parsed_data['main']['temp']

    # Returns a float of temperature in degrees Kelvin (default)
    def getTempK(self):
        return self.temp_kelvin

    # Returns a float of temperature in degrees Farenheit
    def getTempF(self):
        return self.getTempK() * (9.0/5) - 459.67

#TEMPORARY DEBUG CODE

loc = gps.getLocation()
w = Weather(loc.getLongitude(), loc.getLatitude())

print "temp: " + repr(w.getTempF())
