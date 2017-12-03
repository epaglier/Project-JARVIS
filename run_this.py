import speech_recognition as sr
from gtts import gTTS
import random
import time
import RPi.GPIO as GPIO
import os

#Random welcome phrases
#welcome = ["I'm up! What did I miss?","Hello world! How can I help you today?","Hello! Lovely day isn't it?"]

welcome = ["This is a really long message that will likely cause our application to crash."]

#Say welcome phrase
#tts = gTTS(text=random.choice(welcome), lang='en')
#tts.save("good.mp3")
#os.system("mpg321 good.mp3")


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
    print(userSay)
    if userSay[0] == 'Echo':
        userString = ""
        for i in range(1,len(userSay)):
            userString = userString + userSay[i]
            userString = userString + " "
        tts = gTTS(text=userString, lang='en')
        tts.save("good.mp3")
        print userString
            #os.system("mpg321 good.mp3")
    else:
        tts = gTTS(text="Sorry I don't understand what you mean by " + userString, lang='en')
        tts.save("good.mp3")
            #os.system("mpg321 good.mp3")
        print userString
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

