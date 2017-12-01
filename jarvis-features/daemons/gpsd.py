import sys
import time
import subprocess
import os

# get a module from a different directory
sys.path.insert(0, '../gps_modules/')

import gps

signal = False
#DEBUG signal = True
while(True):
    time.sleep(5)
    loc = gps.getLocation()
    if loc.getFix() and not signal:
        # no signal -> signal
        subprocess.check_output(["/bin/mimic/mimic", "-t", "\"GPS signal established.\""])
        signal = True
        print "[gpsd] GPS signal established."
    elif not loc.getFix() and signal:
        # signal -> no signal
        subprocess.check_output(["/bin/mimic/mimic", "-t", "\"GPS signal lost.\""])
        signal = False
        print "[gpsd] GPS signal lost."
