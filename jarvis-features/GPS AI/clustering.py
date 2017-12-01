import sys
import math
import datetime
#from geopy.distance import great_circle

inputTextFile = "output.txt"#sys.argv[1]
distThresh = .01 #mile
radius = distThresh
#open file
data = open(inputTextFile)

#Create set with format format time,latitude,longitude,velocity from download.py style
def Parse(s):
	tem = s.split(",")
	list = [str(tem[0].split(": ")[1]),str(tem[1].split(": ")[1]),str(tem[2].split(": ")[1]),str(tem[3].split(": ")[1].split(" ")[0])]
	return list

def distance(point1, point2):
	#latlong1 = (float(point1[1]),float(point1[2]))
	#latlong2 = (float(point2[1]),float(point2[2]))
	return math.sqrt(math.pow(float(point1[1]) - float(point2[1]),2) + math.pow(float(point1[2]) - float(point2[2]),2))
	#return great_circle(latlong1, latlong2).miles
#test parse
def testParse():
	pointDataString = data.readline()
	print pointDataString
	while pointDataString != None:
		print Parse(pointDataString)
		data.readline()
		pointDataString = data.readline()
		if "Number of entries: " in pointDataString:
			break

#testParse()

def getAllPoints():
	setOfAll = []
	pointDataString = data.readline()
	#print pointDataString
	while pointDataString != None:
		setOfAll.append(Parse(pointDataString))
		data.readline()
		pointDataString = data.readline()
		if "Number of entries: " in pointDataString:
			break
	return setOfAll

#testAllPoints
#print getAllPoints()
#print "Loading list..."
pointlist = getAllPoints()
#print "Loaded"

#adds ranking to loaded list (finds num neighbors within range)
def rankAll():
	rankedPointz = []
	for point in pointlist:
		#print "Running rank for point " + str(point[0]) + "..."
		numNeighbors = 0
		for point2 in pointlist:
			if point != point2 and distance(point,point2) < distThresh:
				numNeighbors = numNeighbors + 1
				#iprint distance(point,point2)
		point.append(numNeighbors)
		rankedPointz.append(point)
		#print point[4]
	return rankedPointz

#legacy
def sortList(points):
	#print "Filtering List"
	ranked_points = []
	ranked_points.append(points[0])
	for point in points:
		insert = False
		for i in range(0,len(ranked_points)):
			if distance(point,ranked_points[i]) > radius:
				ranked_points.insert(i, point)
				#print "Inserting " + point[0] + ": value=" + str(point[4]) +": At position " + str(i)
				insert = True
				break
			elif point[4] > ranked_points[i][4]:
				ranked_points.remove(ranked_points[i])
				ranked_points.insert(i,point)
				#print "Replacing"
				break
	return ranked_points

	
#print filterList(rankAll())

def reduce(points):
	newPointList = []
	for point in points:
		nah = True
		for newPoint in newPointList:
			if (point[4] <= newPoint[4] and distance(newPoint,point) < radius) or point[4] < 10:
				nah = False
		if nah:
			newPointList.append(point)
	return newPointList
								

#def plot(points):
#	x_axi = []
#	y_axi = []
#	for point in points:
#		x_axi.append(float(point[1]))
#		y_axi.append(float(point[2]))
#		print point[1] + "," + point[2]
#	plt.plot(x_axi,y_axi, 'ro')
#	plt.ylabel('Latitude')
#	plt.xlabel('Longetude')
	#plt.axis([38, 42, -90, -85])
#	plt.show()
def get():
	list = rankAll()
	sortedList = sortList(list)
	reduct = reduce(sortedList)
	return reduct

def getWalkTime(day):
	i = True
	last = ""
	totTime = 0
	for point in pointlist:
		if not i:
			speed = float(point[3])
			if speed > 1 and speed < 5:
				time1 = datetime.datetime.strptime(last[0], '%Y-%m-%d %H:%M:%S')	
				time2 = datetime.datetime.strptime(point[0], '%Y-%m-%d %H:%M:%S')
				hours, remainder = divmod((time2-time1).seconds, 3600)
				minutes, seconds = divmod(remainder, 60)
				if time1.day == day:
					totTime = totTime + seconds
				
		last = point
		i = False
	return totTime
#plot(reduct)
