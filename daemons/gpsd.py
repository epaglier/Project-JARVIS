import sys
import time
import subprocess
import os

# get a module from a different directory
user = os.getlogin()
sys.path.insert(0, '/home/' + user + '/mycroft-core/gps_modules/')

import gps

signal = False
#DEBUG signal = True
while(True):
    time.sleep(5)
    loc = gps.getLocation()
    if loc.getFix() and not signal:
        # no signal -> signal
        subprocess.check_output(["../mimic/mimic", "-t", "\"GPS signal established.\""])
        signal = True
        print "[gpsd] GPS signal established."
    elif not loc.getFix() and signal:
        # signal -> no signal
        subprocess.check_output(["../mimic/mimic", "-t", "\"GPS signal lost.\""])
        signal = False
        print "[gpsd] GPS signal lost."
