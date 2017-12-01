import urllib2
import json

GOOGLE_MAPS_API_KEY = "AIzaSyBMK5WI2yWUnBpnToA7FX0bKf8Lkb3RWBQ"

def getFormatForLoc(latitude,longitude):
    maps_query = "https://maps.googleapis.com/maps/api/geocode/json?latlng=" + str(latitude) +"," + str(longitude) + "&key=" + GOOGLE_MAPS_API_KEY
    response = urllib2.urlopen(maps_query).read()
    parsed_data = json.loads(response)

    return parsed_data['results'][0]['formatted_address']

