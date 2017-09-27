import gps
import datetime
import mysql.connector

cnx = mysql.connector.connect(user='pi', password='sudo', database='test')
cursor = cnx.cursor()
while True:
    stringToSend = ("INSERT INTO gps (time, latitude, longitude, velocity) VALUES (%s, %s, %s, %s)")
    loc = gps.getLocation()
    latitude = str(loc.getLatitude())
    print latitude
    longitude = str(loc.getLongitude())
    print longitude
    velocity = str(loc.getVelocity())
    print velocity
    data= (datetime.datetime.now(), latitude, longitude, velocity)
    cursor.execute(stringToSend, data)
    cnx.commit()
    print "uploaded"
