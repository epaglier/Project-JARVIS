import urllib2
import json
import os
import sys
import subprocess
import random

# Used to randomly select a joke source
rand = random.randint(0, 2)

if rand == 0:
    with open(os.devnull, 'w') as devnull:
        joke = subprocess.check_output(["curl", "-H", "\"Accept: text/plain\"", "https://icanhazdadjoke.com/"], stderr=devnull)
    subprocess.check_output(["/bin/mimic/mimic", "-t", joke])
    print joke

elif rand == 1:
    response = urllib2.urlopen("https://08ad1pao69.execute-api.us-east-1.amazonaws.com/dev/random_joke").read()
    parsed_data = json.loads(response)
    joke = parsed_data['setup'] + "\n" + parsed_data['punchline']
    subprocess.check_output(["/bin/mimic/mimic", "-t", joke])

else:
    response = urllib2.urlopen("http://api.yomomma.info/").read()
    parsed_data = json.loads(response)
    subprocess.check_output(["/bin/mimic/mimic", "-t", parsed_data['joke']])


