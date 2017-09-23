import serial
import sys
import math


fix_type = 0
longitude_degs = None
latitude_degs = None
altitude_meters = None
velocity_meters = None

stream = serial.Serial('/dev/ttyS0') #configure serial reader

# Returns longitude as float, updates every 1s
# Returns None if satelite lock lost or on cold start
def getLongitude():
    return longitude_degs

# Returns latitude as float, updates every 1s
# Returns None if satelite lock lost or on cold start
def getLatitude():
    return latitude_degs

# Returns altitude above sea level in meters, updates every 1s
# Returns None if satelite lock lost or on cold start
def getAltitude():
    return altitude_meters

# Returns fix type as int, updates every 1s
# 0: No satellite lock
# 1: 2D fix, long & lat available
# 2: 3D fix, long, lat & alt available
def getFixType():
    return int(fix_type)

# Returns velocity of device in meters/second, updates every 1s
# Returns None if statelite lock lost or on cold start
def getVelocity():
    return velocity_meters

#continuously polls for updates to GPS data
while True:
    NEMA = ''
    while True:
        char = stream.read()
        if char == '$': #$ delimits the start of a NEMA sentence
            break
        NEMA += char
    
    NEMA_tokens = NEMA.split(',')
    if NEMA[0:5] == 'GPGGA': #contains most important info
        fix_type = NEMA_tokens[6]
        if fix_type == 2: #3D tracking available
            altitude_meters = float(NEMA_tokens[9])
        else:
            altitude_meters = None
        if fix_type != 0: #Only 2D tracking avaiable
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
        else: #No satelite lock
            latitude_degs = None
            longitude_degs = None
        
    if NEMA[0:5] == 'GPRMC': #Contains info on velocity in knots
        if fix_type != 0:
            velocity_meters = 0.514444 * float(NEMA_tokens[7])
        else:
            velocity_meters = None
    
