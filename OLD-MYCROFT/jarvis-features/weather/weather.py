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
        self.humidity = parsed_data['main']['humidity']
        self.precipitation = parsed_data['weather'][0]['description']
        self.wind = parsed_data['wind']['speed']

    # Returns a float of temperature in degrees Kelvin (default)
    def getTempK(self):
        return self.temp_kelvin

    # Returns a float of temperature in degrees Farenheit
    def getTempF(self):
        return self.getTempK() * (9.0/5) - 459.67
    
    # Returns a float of temperature in degrees Celcius
    def getTempC(self):
        return self.getTempK() - 273.15
    
    # Returns humidity as a percentage
    def getHumidity(self):
        return self.humidity

    # Returns a string representing cloud cover/rain/etc.
    # see https://openweathermap.org/weather-conditions for details
    def getPrecipitation(self):
        return self.precipitation

    # Returns wind speed in meters / second
    def getWind(self):
        return self.wind

# Returns the current weather at the given coordinates
def getWeather(longitude, latitude):
    return Weather(longitude, latitude)

# Helper function that returns the weather at JARVIS's current location
def getWeatherHere():
    loc = gps.getLocation()
    return getWeather(loc.getLongitude(), loc.getLatitude())
