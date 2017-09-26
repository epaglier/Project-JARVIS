import serial
import sys
import math

stream = serial.Serial('/dev/ttyS0')

def _getGPRMCToken(index):
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

    NEMA_tokens = NEMA.split(',')
    return NEMA_tokens[index]

# Returns True if there is a satelite fix
# Returns False if no satelite lock
def getFix():
    return (_getGPRMCToken(2) == 'A')

# Returns longitude as a float
# Will return None if no satelite lock
def getLongitude():
    if getFix():
        token = _getGPRMCToken(4)
        longitude_degs = int(float(token)) / 100
        longitude_mins = float(token) - (longitude_degs * 100)
        longitude_degs += longitude_mins / 60
        if _getGPRMCToken(5) == 'W':
            longitude_degs *= -1
        return longitude_degs
    else:
        return None

# Returns latitude as a float
# Will return None if no satelite lock
def getLatitude():
    if getFix():
        token = _getGPRMCToken(2)
        latitude_degs = int(float(token)) / 100
        latitude_mins = float(token) - (latitude_degs * 100)
        latitude_degs += latitude_mins / 60
        if _getGPRMCToken(3) == 'S':
            latitude_degs *= -1
        return latitude_degs
    else:
        return None

# Returns velocity in m/s
# Will return None if no satelite lock
def getVelocity():
    if getFix():
        token = float(_getGPRMCToken(7))
        return token * 0.514444
    else:
        return None
