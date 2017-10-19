import time
import new_gps


time.sleep(1) #wait for NMEA sentences to arrive
N = new_gps.getLocation()

print "Velocity: " + repr(N.getVelocity())
print "Fix: " + repr(N.getFix())

