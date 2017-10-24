import time
import gps

N = gps.getLocation()

print "Velocity: " + repr(N.getVelocity())
print "Fix: " + repr(N.getFix())

print "sleeping 2 seconds"

time.sleep(2)

print "getting a new location"
new = gps.getLocation()
print "Velocity: " + repr(new.getVelocity())
time.sleep(.1)
