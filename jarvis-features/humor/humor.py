import urllib2
import json
import os
import sys
import subprocess
import random

# Used as a cache when no network is available
cache = []

# Used to randomly select a joke source
rand = random.randint(0, 2)

temp = subprocess.check_output(["curl", "http://api.yomomma.info/"])
if "curl: (6) Could not resolve host: api.yomomma.info" == temp:
    if len(cache) > 0:
        joke = cache.pop(len(cache) - 1)
        subrocesss.check_output(["/bin/mimic/mimic", "-t", joke])
    else:
        # No wifi/API unavailable
        subrocesss.check_output(["/bin/mimic/mimic", "-t", "I can't make a joke now, sorry."])
        sys.exit() # This could be wrong and cause a crash
while len(cache) < 5:
    if rand == 0:
        with open(os.devnull, 'w') as devnull:
            joke = subprocess.check_output(["curl", "-H", "\"Accept: text/plain\"", \
                    "https://icanhazdadjoke.com/"])
            cache.append(joke)
    elif rand == 1:
        response = urllib2.urlopen("https://08ad1pao69.execute-api.us-east-1.amazonaws.com/dev/random_joke").read()
        parsed_data = json.loads(response)
        joke = parsed_data['setup'] + "\n" + parsed_data['punchline']
        cache.append(joke)

    else:
        response = urllib2.urlopen("http://api.yomomma.info/").read()
        parsed_data = json.loads(response)
        #subprocess.check_output(["/bin/mimic/mimic", "-t", parsed_data['joke']])
        cache.append(parsed_data['joke'])


subprocess.check_output(["/bin/mimic/mimic", "-t", cache.pop(len(cache) - 1)])
print cache.pop(len(cache) - 1)
#print "cache length: " + repr(len(cache))
