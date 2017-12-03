import speech_recognition as sr
from gtts import gTTS
import random
import time
#import RPi.GPIO as GPIO
import importlib
import os

#Random welcome phrases
#welcome = ["I'm up! What did I miss?","Hello world! How can I help you today?","Hello! Lovely day isn't it?"]

#Say welcome phrase
#tts = gTTS(text=random.choice(welcome), lang='en')
#tts.save("good.mp3")
#os.system("mpg321 good.mp3")

skillList = []
for skill in os.listdir("ourSkillz"):
    if not skill.split(".")[0] == "__init__" and not skill.split(".")[0] == "__pycache__" and skill.split(".")[1] == 'py':
        skillList.append(importlib.import_module("ourSkillz." + skill[:-3]))
print(skillList)
# obtain audio from the microphone
r = sr.Recognizer()

with sr.Microphone() as source:
            # recognize speech using Google Speech Recognitioin
    print("say something!")
    audio = r.listen(source,timeout = 2,phrase_time_limit = 5)
try:
                    # for testing purposes, we're just using the default API key
                        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
                            # instead of `r.recognize_google(audio)`
    print("recognizing..")
    userString = r.recognize_google(audio)
    userSay = userString.split(" ")
    
    highestResponseValue = 0
    mostFitSkill = None

    for skill in skillList:
        value = skill.respond(userSay)
        if (value > highestResponseValue):
            highestResponseValue = value
            mostFitSkill = skill
    if mostFitSkill != None: 
        tts = gTTS(text=mostFitSkill.handle_input(userString), lang='en')
        tts.save("good.mp3")
        os.system("mpg321 good.mp3")
        exit()
    else:
        tts = gTTS(text="I don't understand what you mean by " + userString, lang='en')
        tts.save("good.mp3")
        os.system("mpg321 good.mp3")
        exit() 
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

