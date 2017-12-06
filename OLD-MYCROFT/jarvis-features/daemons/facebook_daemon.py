from facepy import GraphAPI

access_token = "EAACEdEose0cBAGFZBcP4ZBlktGHxwctIJh9Ab4vGHIS8NgEc5ZBmPbIsBZCZCdlp2onAkMPkbzd5Ao3YPaYZAuY5eeZCoz5KzHAnRkXpjeVArBaptXU5w2dSqBiO6ZCZBiHT84ScZAmm8n7Ay0OZC0oY3LbnCvT9NfdR54qMSYkPcQTU2OZCJyZCzWxs3FAvVQMNnLMj2ZBUhZAbCBtRQZDZD"

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
