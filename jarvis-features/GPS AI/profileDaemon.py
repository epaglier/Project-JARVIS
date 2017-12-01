import time
import makeProfile
import gps

try:
	file = open("profile.txt")
	file.readline()
	file.readline()
	file.readline()
	file.readline()
	location = file.readline()
	while location != "":
		#Calculate time to destination
		print(location)
		location = file.readline()
except:
	makeProfile.make()
