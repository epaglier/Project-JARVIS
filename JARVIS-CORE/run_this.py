import speech_recognition as sr
from gtts import gTTS
import random
import time
import RPi.GPIO as GPIO
import importlib
import os
import sys
import ourSkillz.dependencies.gps as gps
import urllib2
import re
import pyttsx

engine = pyttsx.init()

def internet_on():
    try:
        urllib2.urlopen('http://www.google.com', timeout=1)
        return True
    except urllib2.URLError as err: 
        return False

#Random welcome phrases
welcome = ["I'm up! What did I miss?","Hello world! How can I help you today?","Hello! Lovely day isn't it?"]

#Debug setup
debug = 0
if len(sys.argv) == 2 and sys.argv[1] == "1":
    debug = 1

def say(string):
    if string == "":
        return
    try:
        #loc = gps.getLocation()
        loc = gps.Location(1, 40.426821, -86.916308, 0.000012)
        string = re.sub('\[loc_coords\]', re.sub('\.', " point ", repr(loc.getLatitude())) + " degrees latitude, " +\
            re.sub('\.', " point ", repr(loc.getLongitude())) + " degrees longitude", string)
        string = re.sub('\[loc_address\]', loc.getFormattedAddress(), string)
        tts = gTTS(text=string, lang='en')
        tts.save("good.mp3")
        os.system("mpg321 good.mp3")
    except Exception:
        tts = gTTS(text=string, lang='en')
        tts.save("good.mp3")
        os.system("mpg321 good.mp3")
    
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)
GPIO.output(21, GPIO.LOW)

GPIO.setup(12, GPIO.IN)
print(GPIO.input(12))
"""INITIALIZATION"""
#Say welcome phrase

skillList = []
for skill in os.listdir("ourSkillz"):
    if not skill.split(".")[0] == "__init__" and not skill.split(".")[0] == "__pycache__" and len(skill.split(".")) > 1 and skill.split(".")[1] == 'py':
        skillList.append(importlib.import_module("ourSkillz." + skill[:-3]))
#print(skillList)
r = None
if not debug:
    with sr.Microphone() as source:
        r = sr.Recognizer()
        r.adjust_for_ambient_noise(source, duration = 1)
#Main function to record and work with input

if not debug:
    say(random.choice(welcome))
else:
    print(random.choice(welcome))

def main():
    if GPIO.input(12):
        if not debug:
            if internet_on(): 
                #get input message
                with sr.Microphone() as source:
                    print("say something!")
                    GPIO.output(21, GPIO.HIGH)
                    audio = r.listen(source)
                    GPIO.output(21, GPIO.LOW)
                try:
                    print("recognizing..")
                    userString = r.recognize_google(audio)
                except sr.UnknownValueError:
                    print("Google Speech Recognition could not understand audio")
                    say("Could you say that again? I couldnt hear you")
                    return
                except sr.RequestError as e:
                    print("Could not request results from Google Speech Recognition service; {0}".format(e))
                    say("Sorry I had an error talking to google try again in a few minutes")
                    return
            else:
                engine.say('Sorry for my raspy voice, I can not seem to reach my voice servers')
                engine.runAndWait()
        else:
            userString = raw_input("(debug) Type something:")
        userSay = userString.split(" ")
    
        highestResponseValue = 0
        mostFitSkill = None

        for skill in skillList:
            value = skill.respond(userSay)
            if (value > highestResponseValue):
                highestResponseValue = value
                mostFitSkill = skill
        if mostFitSkill != None: 
            print(userSay) 
            print("janice" in userSay) #Make userstring the lat and long
            if debug:
                string = mostFitSkill.handle_input(userString)
                loc = gps.Location(1, 40.426821, -86.916308, 0.000012)
                string = re.sub('\[loc_coords\]', repr(loc.getLatitude())+" degrees latitude, " +\
                    repr(loc.getLongitude()) + " degrees longitude", string)
                string = re.sub('\[loc_address\]', loc.getFormattedAddress(), string)

                print(string)
            else:
                string = mostFitSkill.handle_input(userString)
                loc = gps.Location(1, 40.426821, -86.916308, 0.000012)
                string = re.sub('\[loc_coords\]', repr(loc.getLatitude())+" degrees latitude, " +\
                    repr(loc.getLongitude()) + " degrees longitude", string)
                string = re.sub('\[loc_address\]', loc.getFormattedAddress(), string)

                print(string)
                say(mostFitSkill.handle_input(userString))
        else:
            if "exit" in userSay:
                print("see you later sir!")
                exit()
            if debug:
                print("I don't understand what you mean by " + userString)
            else:
                say("I don't understand what you mean by " + userString)
while True:
    main()
    time.sleep(.1)
