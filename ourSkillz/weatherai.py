from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
import numpy as np
import dependencies.weather as weather

respond_to = ["what","should","I","wear","today"]

def respond(array):
    count = 0
    for word in array:
        if word in respond_to:
            count = count + 1
    return count

def handle_input(string):
    temp = weather.getWeather(-86.9191637,40.4277277).getTempF()
    print(temp)
    return "Its about " + str(temp) + " degrees fahrenheit, I suggest wearing a " + predictClothesData(temp)[0]

def predictClothesGeneral(temp):
        dataFile = open("data.txt")

        data = dataFile.read()

        data = data.split("\n")
        X = []
        Y = []
        Y2 = []
        for i in range(0,len(data) - 1):
                X.append([float(data[i].split(":")[1])])
                Y.append(int(data[i].split(":")[3]))
                Y2.append(int(data[i].split(":")[4]))
        clf = RandomForestClassifier(n_estimators=25)
        clf2 = RandomForestClassifier(n_estimators=25)
        clf.fit(X,Y)
        clf2.fit(X,Y2)
        pants = clf.predict([[temp]])
        tops = clf2.predict([[temp]])

        s = "I recommend you wear a pair of "
        if pants == 1:
                s = s + "jeans"
        else:
                s = s + "khaki shorts"

        s = s + " and a "

        if tops == 1:
                s = s + "shirt, its a nice day out!"
        elif tops == 2:
                s = s + "sweat shirt."
        else:
                s = s + "jacket, it will be chilly today."

        return s

def predictFromFileGeneral(fileName):
        fi = open(fileName)
        data = fi.read().split("\n")
        for i in range(0,len(data) - 1):
                data2 = data[i].split(":")
                print "At " + data2[1].split(",")[0] + " degrees... " + predictClothesGeneral(float(data2[1].split(",")[0]))

def addToKnownList(shirt, temp):
        dataFile = open("userAdded.txt", 'a')
        dataFile.write(str(shirt + ":" + str(temp)) + '\n')

def predictClothesData(temp):
        dataFile = open("./ourSkillz/userAdded.txt")

        data = dataFile.read()

        data = data.split("\n")
        X = []
        Y = []
        for i in range(0,len(data) - 1):
                X.append([float(data[i].split(":")[1])])
                Y.append(data[i].split(":")[0])
        clf = RandomForestClassifier(n_estimators=25)
        clf.fit(X,Y)
        predict = clf.predict([[temp]])

        return predict

def predictFromFileData(fileName):
        fi = open(fileName)
        data = fi.read().split("\n")
        for i in range(0,len(data) - 1):
                data2 = data[i].split(":")
                print "At " + data2[1].split(",")[0] + " degrees... I would recommend a " + predictClothesData(float(data2[1].split(",")[0]))[0]
