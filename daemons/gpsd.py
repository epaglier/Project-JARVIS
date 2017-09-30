import sys
import time

sys.path.append('home/daniel/mycroft-core/gps_modules')
import gps

signal = False

while(True):
    time.sleep(5)
    loc = gps.getLocation()
    if loc.getFix() and not signal:
        # no signal -> signal
        #TODO speak = subprocess.check_output(["mimic", "-t", "GPS signal established."])
        signal = True
        print "[gpsd] GPS signal established."
    elif not loc.getFix() and signal:
        # signal -> no signal
        #TODO speak = subprocess.check_output(["mimic", "-t", "GPS signal lost."])
        signal = False
        print "[gpsd] GPS signal lost."
