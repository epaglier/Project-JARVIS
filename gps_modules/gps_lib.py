import serial
import sys
import math


fix_type = 0
longitude_degs = None
latitude_degs = None
altitude_meters = None

stream = serial.Serial('/dev/ttyS0') #configure serial reader

# Returns longitude as float, updates every 1s
def getLongitude():
    return float(longitude_degs)

# Returns latitude as float, updates every 1s
def getLatitude():
    return float(latitude_degs)

# Returns altitude above sea level in meters, updates every 1s
# Will return None if no satelite lock
def getAltitude():
    return altitude_meters

# Returns fix type as int, updates every 1s
# 0: No satellite lock
# 1: 2D fix, long & lat available
# 2: #D fix, long, lat & alt available
def getFixType():
    return int(fix_type)

#continuously polls for updates to GPS data
while True:
    NEMA = ''
    while True:
        char = stream.read()
        if char == '$': #$ delimits the start of a NEMA sentence
            break
        NEMA += char
    if NEMA[0:5] == 'GPGGA': #contains most important info
        NEMA_tokens = NEMA.split(',')
        latitude_degs = int(float(NEMA_tokens[2])) / 100
        latitude_mins = float(NEMA_tokens[2]) - (latitude_degs * 100)
        latitude_degs += latitude_mins / 60
        if NEMA_tokens[3] == 'S': #negative degs for southern hemisphere
            latitude_degs *= -1
        longitude_degs = int(float(NEMA_tokens[4])) / 100
        longitude_mins = float(NEMA_tokens[4]) - (longitude_degs * 100)
        longitude_degs += longitude_mins / 60
        if NEMA_tokens[5] == 'W': #negative degs for western hemisphere
            longitude_degs *= -1 
        fix_type = NEMA_tokens[6]
        if fix_type != 0:
            altitude_meters = float(NEMA_tokens[9])
        else:
            altitude = None
        
