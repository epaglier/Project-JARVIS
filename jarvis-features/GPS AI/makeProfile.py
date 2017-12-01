import os

def make():
	list = os.listdir("./DailySummaries")
	size = len(list)

	listOfLocs = ""
	tot = 0

	for f in list:
		file = open("./DailySummaries/" + f)
		file.readline()
		time = file.readline().split(" hours ")
		hours = int(time[0])
		time = time[1].split(" minutes ")
		minutes = int(time[0])
		time = time[1].split(" seconds")
		seconds = int(time[0])
		hours = hours*3600
		minutes = minutes*60
		tot = tot + hours + minutes + seconds
		file.readline()
		file.readline()
		file.readline()
		file.readline()
		file.readline()
		next = file.readline()
		while next != "":
			listOfLocs = listOfLocs + next
			next = file.readline()
	file = open("profile.txt","w+")
	file.write("Average walking time over " + str(size) + " days\n" + str(int(float(tot)/size)/3600) + "," + str(int(float(tot)/size)/60) + "," + str(int(float(tot)/size)%60) + "\n\n" + "Locations:\n" + listOfLocs)
