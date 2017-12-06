import time
import tweepy
import os
from gtts import gTTS 
import subprocess

consumer_key = "ARfkWvjcYO1YFtl01ERTgDzbv"
consumer_secret = "aQjhoOQtx45vYu1pOSvq5p1Im1drj8kuRKtCZnzBBazovUccnX"
access_token="933075473399246849-BUYqU5ioK2mbLCj7beGuOLkqPY7W0Fs"
access_token_secret="TUpB14OSRpJvKn9NPY8NwqLqdM6y2UYUEhocHx7obpXAM"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
newestTweet = public_tweets[0]
currTweet = public_tweets[0]

while True:
	if newestTweet.text != currTweet.text:
		for tweet in public_tweets:
			if tweet.text == currTweet.text:
				break
                        result = newestTweet.user.screen_name + " tweeted: " + newestTweet.text
                        tts = gTTS(text = result, lang = "en")
                        tts.save("twitter.mp3")
                        os.system("mpg321 twitter.mp3")
		currTweet = newestTweet

	time.sleep(71)
	public_tweets = api.home_timeline()
	newestTweet = public_tweets[0]
