import serial
import thread
import threading
import sys
import time
import atexit
import urllib2
import json
import re

printed_done = False
initialized = False
exiting = False
sys.stdout.write("Initializing... ")
sys.stdout.flush()

GOOGLE_MAPS_API_KEY = "AIzaSyBMK5WI2yWUnBpnToA7FX0bKf8Lkb3RWBQ"

stream = serial.Serial('/dev/ttyS0')

class Location:

    # Constructor
    # Pass in various variables to create it
    def __init__(self, _fix, _longitude, _latitude, _velocity):
        self.formatted_address = "Address unavailable"
        if _fix:
            maps_query = "https://maps.googleapis.com/maps/api/geocode/json?latlng=" + repr(_latitude) +"," + repr(_longitude) + "&key=" + GOOGLE_MAPS_API_KEY
            response = urllib2.urlopen(maps_query).read()
            parsed_data = json.loads(response)

            self.formatted_address = parsed_data['results'][0]['formatted_address']

        self.fix = _fix
        self.longitude = _longitude
        self.latitude = _latitude
        self.velocity = _velocity

    # Returns a fromatted string in the form
    # Number Street, Municipality, State Zip, Country
    def getFormattedAddress(self):
        return self.formatted_address
    
    # Returns the distance in km to a destination from the current location
    # _mode accepts "driving", "walking", "bicycling"
    # Note: _destination is NOT sanitized so don't f*ck it up
    # Note: Also don't include whitespace in _destination
    def getDistTo(self, _destination, _mode):
        if _mode != "driving" and _mode != "walking" and _mode != "bicycling":
            return -1 # sanitize inputs (security)
        if not self.fix:
            return -2 # only do this if we have a GPS lock
        request = "https://maps.googleapis.com/maps/api/distancematrix/json?units=metric&mode=" + _mode + "&origins=" + repr(self.latitude) + "," + repr(self.longitude) + "&destinations=" + _destination + "&key=" + GOOGLE_MAPS_API_KEY
        response = urllib2.urlopen(request).read()
        parsed_data = json.loads(response)
        return parsed_data['rows'][0]['elements'][0]['distance']['value']/1000.0
    
    # Returns the directions to a destination from the current location
    # _mode accepts "driving", "walking", "bicycling"
    # Note: _destination is NOT sanitized so don't f*ck it up
    # Note: Also don't include whitespace in _destination
    def getDirectionsTo(self, _destination, _mode):
        if _mode != "driving" and _mode != "walking" and _mode != "bicycling":
            return "Directions unavailable Err code 1" # sanitize inputs (security)
        if not self.fix:
            return "Directions unavailable Err code 2" # only do this if we have a GPS lock
        request = "https://maps.googleapis.com/maps/api/directions/json?units=metric&mode=" + _mode + "&origin=" + repr(self.latitude) + "," + repr(self.longitude) + "&destination=" + _destination + "&key=" + GOOGLE_MAPS_API_KEY
        response = urllib2.urlopen(request).read()
        parsed_data = json.loads(response)
        directions = ""
        for step in parsed_data['routes'][0]['legs'][0]['steps']:
            # Regex ~magic~
            current = re.sub('<\/div>', '', step['html_instructions'])
            current = re.sub('<div[^<>]*>', '\n', step['html_instructions'])
            current = re.sub('<[^<>]*>', '', current)
            directions += current + "\n"
        return directions

    # Returns True if there is a satelite fix
    # Returns False if no satelite lock
    def getFix(self):
        return self.fix

    # Returns longitude as a float
    # Will return None if no satelite lock
    def getLongitude(self):
        if self.getFix():
            return self.longitude
        return None

    # Returns latitude as a float
    # Will return None if no satelite lock
    def getLatitude(self):
        if self.getFix():
            return self.latitude
        return None

    # Returns velocity in m/s as a float
    # Will return None if no satelite lock
    def getVelocity(self):
        if self.getFix():
            return self.velocity
        return None

    # Returns transportation type as an int
    # -1 - Error (outside expected range)
    #  0 - Walking/jogging/running
    #  1 - Biking/small wheels/jogging/running
    #  2 - Car/large vehicle
    def getTransportation(self):
        if self.getFix():
            vel = self.getVelocity()
            if vel < 3: # about 6.7 mph
                return 0
            elif vel < 7: # about 15.7 mph
                return 1
            elif vel < 70: # about 157 mph
                return 2
        return -1 # wtf this person's doing 160

def _getGPRMC():
    while True:
        NEMA = ""
        while stream.read() != '$':
            #do nothing; advance stream to start of GPRMC sentence
            pass
        id = stream.read(5) #Should be of form 'GP___'
        if id == 'GPRMC':
            break
    NEMA = ""
    while True:
        char = stream.read()
        if char != '$':
            NEMA += char
        else:
            break
    return NEMA

def _getLocation():
    NEMA = _getGPRMC()
    tokens = NEMA.split(',')
    fix = tokens[2] == 'A' # boolean
    if fix:
        longitude_degs = int(float(tokens[5])) / 100
        longitude_mins = float(tokens[5]) - (longitude_degs * 100)
        longitude_degs += longitude_mins / 60
        if tokens[6] == 'W':
            longitude_degs *= -1

        latitude_degs = int(float(tokens[3])) / 100
        latitude_mins = float(tokens[3]) - (latitude_degs * 100)
        latitude_degs += latitude_mins / 60
        if tokens[4] == 'S':
            latitude_degs *= -1

        velocity = float(tokens[7]) * 0.514444 # convert to meters

        return Location(fix, longitude_degs, latitude_degs, velocity)
    else:
        return Location(fix, None, None, None)

location = Location(0, None, None, None)
lock = None
lock = threading.Lock()

def collect():
    global location
    global initialized
    global exiting
    global lock
    while True:
        location = _getLocation()
        initialized = True
        if exiting:
            sys.stdout.write("Exiting thread... ")
            sys.stdout.flush()
            break
        
# I'd like to do some sort of interrupt for initialization
# but I'm not 100% sure how that would work so now it polls
# every 1/10 of a second.
def getLocation():
    global initialized
    global printed_done
    duration = 0.1
    elapsed = 0
    threshold = 3 # Don't wait longer than 3 seconds for a fix
    while not initialized:
        if duration > threshold:
            sys.stdout.flush()
            return location
        time.sleep(duration) # Yield CPU and poll
        elapsed += duration
    if not printed_done:
        sys.stdout.write("Done\n")
        printed_done = True
    return location

def exit():
    global exiting
    exiting = True
    collector.join() #blocks until collector thread dies
    sys.stdout.write("Done\n")

atexit.register(exit)
collector = threading.Thread(target = collect)
collector.daemon = True
collector.start()

