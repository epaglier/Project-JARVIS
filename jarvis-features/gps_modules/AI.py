import random
import sys
import numpy as np
import mysql.connector
import datetime

def init_board_gauss(N, k):
    n = float(N)/k
    X = []
    for i in range(k):
        c = (random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(-1, 1))
        s = random.uniform(0.05,0.5)
        x = []
        while len(x) < n:
            a, b, d = np.array([np.random.normal(c[0], s), np.random.normal(c[1], s), np.random.normal(c[2], s)])
            # Continue drawing points from the distribution in the range [-1,1]
            if abs(a) < 1 and abs(b) < 1 and abs(d) < 1:
                x.append([a,b,d])
        X.extend(x)
    X = np.array(X)[:N]
    return X

def getDatabaseData():
    cnx = mysql.connector.connect(user='pi', password='sudo', database='test')
    cursor = cnx.cursor()
    querry = ("SELECT * FROM gps") #LIMIT 0, 200")
    cursor.execute(querry)
    x = []
    for (time,longitude,latitude,velocity) in cursor:
        a, b, c, d = np.array([(time - datetime.datetime(1, 1, 1)).total_seconds() * 10000000, longitude, latitude, velocity])
        x.append([a,b,c,d])
    return np.array(x)

def get2DDatabaseData():
   cnx = mysql.connector.connect(user='pi', password='sudo', database='test')
   cursor = cnx.cursor()
   querry = ("SELECT * FROM gps")
   cursor.execute(querry)
   x = []
   for (time,longitude,latitude,velocity) in cursor:
       a, b, c = np.array([longitude, latitude, velocity])
       x.append([a,b,c])
   return np.array(x)
        
def cluster_points(X, mu):
    clusters  = {}
    for x in X:
        bestmukey = min([(i[0], np.linalg.norm(x-mu[i[0]])) \
                for i in enumerate(mu)], key=lambda t:t[1])[0]
        try:
            clusters[bestmukey].append(x)
        except KeyError:
            clusters[bestmukey] = [x]
    return clusters

def reevaluate_centers(mu, clusters):
    newmu = []
    keys = sorted(clusters.keys())
    for k in keys:
        newmu.append(np.mean(clusters[k], axis = 0))
    return newmu

def has_converged(mu, oldmu):
    return (set([tuple(a) for a in mu]) == set([tuple(a) for a in oldmu]))

def find_centers(X, K):
    # Initialize to K random centers
    oldmu = random.sample(X, K)
    mu = random.sample(X, K)
    clusters = []
    while not has_converged(mu, oldmu):
        oldmu = mu
        # Assign all points in X to clusters
        clusters = cluster_points(X, mu)
        # Reevaluate centers
        mu = reevaluate_centers(oldmu, clusters)
    return(mu, clusters)

def getDateFromTicks(ticks):
    return datetime.datetime.min + datetime.timedelta(microseconds = int(ticks)/10)

if (len(sys.argv) < 3):
    print "usage- AI.py [\"2D\" or \"3D\" [number of clusters]]"
elif (sys.argv[1] == "2D"):
    test = find_centers(get2DDatabaseData(), int(sys.argv[2]))
    for i in range(len(test[0])):
        print "Latitude: " + str(test[0][i][0]) + " Longitude: " + str(test[0][i][1]) + " Velocity: " + str(test[0][i][2])
elif (sys.argv[1] == "3D"):
    test = find_centers(getDatabaseData(), int(sys.argv[2]))
    for i in range(len(test[0])):
        print str(getDateFromTicks(test[0][i][0])) + " | Latitude: " + str(test[0][i][1]) + " Longitude: " + str(test[0][i][2]) + " Velocity: " + str(test[0][i][3])
else:
    print "bad"

