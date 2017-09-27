import mysql.connector
from hurry.filesize import size

cnx = mysql.connector.connect(user='pi', password='sudo', database='test')

cursor = cnx.cursor()
querry = ("SELECT * FROM gps LIMIT 0, 100")
cursor.execute(querry)
count = 0

for (time,longitude,latitude,velocity) in cursor:
    print "time: {}, latitude: {}, longitude: {}, velocity: {} m/s\n".format(time, latitude, longitude, velocity)
    count = count +1
print "Number of entries: " + str(count)

cursor2 = cnx.cursor()
cursor2.execute("SELECT data_length FROM information_schema.TABLES WHERE table_name = \"gps\"")

for (data_length) in cursor2:
    print "size: " + size(int(data_length[0]))
