import time
import subprocess

signal = False # Boolean of whether signal has already been lost

while(True):
    wlan = subprocess.check_output(["./ethcheck.sh"])
    time.sleep(5)
    if wlan != "" and not signal: 
        # signal restored. signal False -> True
        subprocess.check_output(["/bin/mimic/mimic", "-t", "\"Network signal restored.\""])
        signal = True
    elif wlan == "" and signal: 
        # signal lost. signal True -> False
        subprocess.check_output(["/bin/mimic/mimic", "-t", "\"Network signal lost.\""])
        signal = False
    
