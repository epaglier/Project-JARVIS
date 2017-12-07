from facepy import GraphAPI

import os
from gtts import gTTS 
import subprocess

access_token = "EAACEdEose0cBADURd9mtCyZBjUCZB2CJqykhpyCt8HkeA3LAPdM04h44FITrKMtoUHLi2H99Dfvb1LNts89Tb20lhGivXmCgCmfKq4N6m5MMf5LsnxbZBGBjAtSQDrsGbd614ZBRhEE9SheBvUF5e7aeo5RhnpIZCsGRgcj5ZCa3k275pYU0zq6Txl5wBHxO4ZD"

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
