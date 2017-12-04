import speech_recognition as sr
from gtts import gTTS
import random
import time
#import RPi.GPIO as GPIO
import importlib
import os
import sys
import urllib2

def internet_on():
    try:
        urllib2.urlopen('http://www.google.com', timeout=1)
        return True
    except urllib2.URLError as err: 
        return False

print(internet_on())

#Random welcome phrases
welcome = ["I'm up! What did I miss?","Hello world! How can I help you today?","Hello! Lovely day isn't it?"]

#Debug setup
debug = 0
if len(sys.argv) == 2 and sys.argv[1] == "1":
    debug = 1

def say(string):
    tts = gTTS(text=string, lang='en')
    tts.save("good.mp3")
    os.system("mpg321 good.mp3")


"""INITIALIZATION"""
#Say welcome phrase
if not debug:
    say(random.choice(welcome))
else:
    print(random.choice(welcome))

skillList = []
for skill in os.listdir("ourSkillz"):
    if not skill.split(".")[0] == "__init__" and not skill.split(".")[0] == "__pycache__" and len(skill.split(".")) > 1 and skill.split(".")[1] == 'py':
        skillList.append(importlib.import_module("ourSkillz." + skill[:-3]))
#print(skillList)

#Main function to record and work with input
def main():
    if not debug:
        if internet_on():
            r = sr.Recognizer()
            #get input message
            with sr.Microphone() as source:
                print("say something!")
                audio = r.listen(source,timeout = 2,phrase_time_limit = 5)
            try:
                print("recognizing..")
                userString = r.recognize_google(audio)
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))
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
        if debug:
            print(mostFitSkill.handle_input(userString))
        else:
            say(mostFitSkill.handle_input(userString))
    else:
        if "exit" in userSay:
            print("see you later sir!")
            exit()
        if debug:
            print("I don't understand what you mean by " + userString)
        else:
            say("I don't understand what you mean by " + userString)

while 1:
    main()
