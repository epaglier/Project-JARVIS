from facepy import GraphAPI
from gtts import gTTS
import os

access_token = "EAACEdEose0cBANBJkveuZCRgkH7S50IMAYZCdqCfDhZA3gKmxIZAABqM8DiU6V6q0d0LWSLmbJDbgLJpZAB8jdzxqDRI2AGZBAzqe5DOFdXZBpf4R8rIlZCEkHUWkPNPJteZB82pggtfAfnFsMGtfTG9IjZAo9uCBnNZCiIFVDjn51HZBqh8z0kv4BdkqVhGaG7RUAO8xW89oCpTmQZDZD"

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
                        print result.encode('utf-8')
                        tts = gTTS(text = "You have a new facebook post! " + s, lang = 'en')
                        tts.save("audio.mp3")
                        os.system("mpg321 audio.mp3")

                currPost = newPost
