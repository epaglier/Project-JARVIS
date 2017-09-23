import serial
import sys
import math

stream = serial.Serial('/dev/ttyS0')

def getGPRMCToken(index):
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

def getFix():
    return (getGPRMCToken(2) == 'A')

def getLongitude():
    if getFix():
        token = getGPRMCToken(5)
        longitude_degs = int(float(token)) / 100
        longitude_mins = float(token) - (longitude_degs * 100)
        longitude_degs += longitude_mins / 60
        if getGPRMCToken(6) == 'W':
            longitude_degs *= -1
        return longitude_degs
    else:
        return None

def getLatitude():
    if getFix():
        token = getGPRMCToken(3)
        latitude_degs = int(float(token)) / 100
        latitude_mins = float(token) - (latitude_degs * 100)
        latitude_degs += latitude_mins / 60
        if getGPRMCToken(4) == 'S':
            latitude_degs *= -1
        return latitude_degs
    else:
        return None
