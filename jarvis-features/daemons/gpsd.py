import sys
import time
from gtts import gTTS
import os

# get a module from a different directory
sys.path.insert(0, '../gps_modules/')

import gps

signal = False
#DEBUG signal = True
while(True):
    time.sleep(5)
    loc = gps.getLocation()
    if loc.getFix() and not signal:
        # no signal -> signal
        established = "\"GPS signal established.\""
        tts = gTTS(text = established, lang = 'en')
        tts.save("audio.mp3")
        os.system("mpg321 audio.mp3")
        signal = True
        print "[gpsd] GPS signal established."
    elif not loc.getFix() and signal:
        # signal -> no signal
        lost = "\"GPS signal lost.\""
        tts = gTTS(text = lost, lang = 'en')
        tts.save("audio.mp3")
        os.system("mpg321 audio.mp3")
        signal = False
        print "[gpsd] GPS signal lost."
