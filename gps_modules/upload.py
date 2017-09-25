import gps
import requests

while True:
    stringToSend = "Longitude: " + str(gps.getLongitude()) + "| Latitude: " + str(gps.getLatitude()) + "| Velocity: " + str(gps.getVelocity())
    requests.post("http://localhost:8008",json={"data": stringToSend})
