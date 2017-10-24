import serial
import thread
import threading
import sys
import time
import atexit

initialized = False
exiting = False
print "Initializing..."

GOOGLE_MAPS_API_KEY = "AIzaSyBMK5WI2yWUnBpnToA7FX0bKf8Lkb3RWBQ"

stream = serial.Serial('/dev/ttyS0')

class Location:

    # Constructor
    # Pass in various variables to create it
    def __init__(self, _fix, _longitude, _latitude, _velocity):
        self.fix = _fix
        self.longitude = _longitude
        self.latitude = _latitude
        self.velocity = _velocity

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

def collect():
    sys.stdout.write("TEST BITCH\n")
    global location
    global initialized
    global exiting
    while True:
        if not initialized:
            initialized = True
        location = _getLocation()
        sys.stdout.write("exiting? " + repr(exiting) + "\n")
        if exiting:
            sys.stdout.write("Exiting thread...")
            break
        
# I'd like to do some sort of interrupt for initialization
# but I'm not 100% sure how that would work so now it polls
# every 1/10 of a second.
def getLocation():
    while not initialized:
        time.sleep(0.1) # Yield CPU and poll
    return location

def exit():
    exiting = True
    sys.stdout.write("in exit()\n")
    time.sleep(1)
    #print "Done"
    sys.stdout.write("Done\n")

atexit.register(exit)
collector = threading.Thread(target = collect)
collector.daemon = True
collector.start()
#thread.start_new_thread(collect, ())

