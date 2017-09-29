# I cannot test this until I have the mimic executable

import time
import subprocess

signal = False # Boolean of whether signal has already been lost

while(True):
    time.sleep(5)
    wlan = subprocess.check_output(["iwconfig", "wlan0"])
    if wlan[10:21] == "IEEE 802.11" and  not signal: 
        # signal restored. signal False -> True
        speak = subprocess.check_output(["mimic", "-t", "Wifi signal restored."])
        signal = True
    elif wlan[10:21] != "IEEE 802.11" and signal: 
        # signal lost. signal True -> False
        speak = subprocess.check_output(["mimic", "-t", "Wifi signal lost."])
        signal = False
    
