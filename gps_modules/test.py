import gps

# Test file

loc = gps.getLocation()

print "Velocity: " + repr(loc.getVelocity())
print "Long: " + repr(loc.getLongitude())
print "Lat: " + repr(loc.getLatitude())
print "Fix: " + repr(loc.getFix())
