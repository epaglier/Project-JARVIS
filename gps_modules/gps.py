import serial

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

# Returns a Location object
# call getter methods to info
def getLocation():
    NEMA = _getGPRMC()
    tokens = NEMA.split(',')
    fix = tokens[2] == 'A' # boolean

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

# Private
# Returns GPRMC NEMA sentences
# Latent GPS connection
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

