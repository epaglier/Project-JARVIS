import gps
import datetime
import mysql.connector

cnx = mysql.connector.connect(user='pi', password='sudo', database='test')
cursor = cnx.cursor()

while True:
    stringToSend = ("INSERT INTO gps (time, longitude, latitude, velocity) VALUES (%s, %s, %s, %s)")
    latitude = str(gps.getLatitude())
    print latitude
    longitude = str(gps.getLongitude())
    print longitude
    data= (datetime.datetime.now(), longitude, latitude, str(gps.getVelocity()))
    cursor.execute(stringToSend, data)
    cnx.commit()
    print "uploaded"
