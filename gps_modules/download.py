import mysql.connector

cnx = mysql.connector.connect(user='pi', password='sudo', database='test')

cursor = cnx.cursor()
querry = ("SELECT * FROM gps LIMIT 0, 100")
cursor.execute(querry)

count = 0
for (time,longitude,latitude,velocity) in cursor:
    print "time: {}, latitude: {}, longitude: {}\n".format(time, longitude,latitude)
    count = count +1
print count
