import importlib
import os
import random
import sys
import time
import urllib2
import RPi.GPIO as GPIO
import speech_recognition as sr
import vlc
from gtts import gTTS
import ourSkillz.dependencies.gps as gps
import re

_SOUND_PIN = 12
_LIGHT_PIN = 21

debug = len(sys.argv) == 2 and (sys.argv[1] == "1" or sys.argv[1] == "debug")

GPIO.setmode(GPIO.BCM)
GPIO.setup(_SOUND_PIN, GPIO.IN)
GPIO.setup(_LIGHT_PIN, GPIO.OUT)
GPIO.output(_LIGHT_PIN, GPIO.LOW)

imported_skills = []
for skill in os.listdir("ourSkillz"):
    if not skill.split(".")[0] == "__init__" \
            and not skill.split(".")[0] == "__pycache__" \
            and len(skill.split(".")) > 1 and skill.split(".")[1] == "py":
        imported_skills.append(importlib.import_module("ourSkillz." + skill[:-3]))

speech_recognition = None
if not debug:
    with sr.Microphone() as source:
        speech_recognition = sr.Recognizer()
        speech_recognition.adjust_for_ambient_noise(source, duration=1)

welcome = ["I'm up! What did I miss?",
           "Hello world! How can I help you today?",
           "Hello! Lovely day isn't it?"]


def say(string):
    if string == "":
        return

    #loc = gps.getLocation()
    loc = gps.Location(1, 40.426821, -86.916308, 0.000012)
    string = re.sub('\[loc_coords\]', re.sub('\.', " point ", repr(loc.getLatitude())) + " degrees latitude, " +\
    re.sub('\.', " point ", repr(loc.getLongitude())) + " degrees longitude", string)
    string = re.sub('\[loc_address\]', loc.getFormattedAddress(), string)
    if "[length_time]" in string:
        destination = string.split(" ").pop()
        print "destination: " + destination
        re.sub('\[length_time\]', loc.getDistTo(destination, "driving"), string)
    try:
        gTTS(string).save("spoken_text.mp3")
        vlc.MediaPlayer("spoken_text.mp3").play()
    except Exception as e:
        print("Could not say: " + string + ". Error: " + e.message)
        return


print("Starting...")

if debug:
    print(random.choice(welcome))
else:
    say(random.choice(welcome))


def internet_on():
    try:
        urllib2.urlopen('http://www.google.com', timeout=5)
        return True
    except urllib2.URLError:
        return False


def main():
    if GPIO.input(_SOUND_PIN):
        if not debug:
            if internet_on():
                with sr.Microphone() as input_source:
                    print("Waiting for input...")
                    GPIO.output(_LIGHT_PIN, GPIO.HIGH)
                    audio = speech_recognition.listen(input_source, timeout=5, phrase_time_limit=5)
                    GPIO.output(_LIGHT_PIN, GPIO.LOW)
                try:
                    print("Recognizing speech...")
                    spoken_text = speech_recognition.recognize_google(audio)
                except sr.UnknownValueError:
                    print("Could not understand speech.")
                    say("Could you say that again? I could not understand you.")
                    return
                except sr.RequestError as e:
                    print("Could not request results from Google Speech Recognition service: " + e)
                    say("Could not reach Google. Please try again later.")
                    return
            else:
                print("No Internet connection.")
                say("I am not currently connected to the internet.")
                return
        else:
            spoken_text = raw_input("(debug):")
        print("User voice input: " + spoken_text)
        spoken_words = spoken_text.split(" ")
        maximum_match_strength = 0
        best_skill_match = None
        for skill in imported_skills:
            try:
                match_strength = skill.respond(spoken_words)
            except Exception as e:
                print("Could not match a skill: " + e.message)
            if match_strength > maximum_match_strength:
                maximum_match_strength = match_strength
                best_skill_match = skill
        if best_skill_match is not None:
            try:
                result = best_skill_match.handle_input(spoken_text)
            except Exception as e:
                print("Could not handle input: " + e.message)
                return
            #loc = gps.getLocation()
            loc = gps.Location(1, 40.426821, -86.916308, 0.000012)
            result = re.sub('\[loc_coords\]', re.sub('\.', " point ", repr(loc.getLatitude())) + " degrees latitude, " +\
            re.sub('\.', " point ", repr(loc.getLongitude())) + " degrees longitude", result)
            result = re.sub('\[loc_address\]', loc.getFormattedAddress(), result)
            print("Skill result: " + result)
            say(result)
        else:
            print("Could not understand command: " + spoken_text)
            say("I am sorry. I could not understand what you said.")


while True:
    main()
    time.sleep(.5)
