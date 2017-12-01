import clustering as cl
import gps
import datetime




def make():
	#Set up current day
	now = datetime.datetime.now()
	nowYear = now.year
	nowMonth = now.month
	nowDay = now.day

	fileName = "dailySummary_" + str(nowMonth) + "_" + str(nowDay) + "_" + str(nowYear) + ".txt"

	file = open(fileName,"w+")
	#Get walking time for the day
	walkTime = cl.getWalkTime(nowDay)
	file.write((str(walkTime/(60*60)) + " hours " + str(walkTime/60) + " minutes " + str(walkTime%60) + " seconds\n"))

	#Get frequented locations for the day
	freqDests = cl.get()
	for dest in freqDests:
		time = datetime.datetime.strptime(dest[0], '%Y-%m-%d %H:%M:%S')
		if nowMonth == time.month and time.day == nowDay:
			file.write(gps.getFormatForLoc(dest[1],dest[2]) + "\n")
