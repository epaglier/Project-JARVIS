import time
import subprocess
from gtts import gTTS
import os

signal = False # Boolean of whether signal has already been lost

while(True):
    wlan = subprocess.check_output(["./ethcheck.sh"])
    time.sleep(5)
    if wlan != "" and not signal: 
        # signal restored. signal False -> True
        os.system("mpg321 audio-established.mp3")
        signal = True
        print "[wifid] Signal established"
    elif wlan == "" and signal: 
        # signal lost. signal True -> False
        os.system("mpg321 audio-lost.mp3")
        print "[wifid] Signal lost"
        signal = False
    
