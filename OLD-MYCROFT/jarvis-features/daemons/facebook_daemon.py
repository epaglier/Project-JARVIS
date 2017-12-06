from facepy import GraphAPI

import os
from gtts import gTTS 
import subprocess
access_token = "EAACEdEose0cBAKrxWuHduuKpuKBSUWiZBJZB8ZBbTDye5oFhsEwi2cWdggTqcQNi6itWepizTPrihXlrrTvA1xELGgNZCWjV5JjceZCZCxZBBQrzENHjI9E57yXjDuM5GNey8GDpFnTRsZB5u6vuVhyFvTgd8x7joIB0o9WI2QUo5r0BCjrWT3Dzf1ZB0l5BAaMHndjiDUolm5AZDZD"
graph = GraphAPI(access_token)
p = graph.get('me/feed')
currPost = p['data'][0]
newPost = p['data'][0]

while True:
	p = []
	p = graph.get('me/feed', fields = ['message','story'])
	newPost = p['data'][0]
	if currPost['id'] != newPost['id']:
		for post in p['data']:
			if currPost['id'] == newPost['id']:
				break
			s = ""
			if "story" in post:
				s = s + post['story']
			if "message" in post:
				s= s+ " " + post['message']
			currPost = post
			result =  "Facebook post: " + s
                        tts = gTTS(text = result, lang = "en")
                        tts.save("facebook.mp3")
                        os.system("mpg321 facebook.mp3")
		currPost = newPost
