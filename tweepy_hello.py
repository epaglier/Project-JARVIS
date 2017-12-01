import tweepy

consumer_key = "ARfkWvjcYO1YFtl01ERTgDzbv"
consumer_secret = "aQjhoOQtx45vYu1pOSvq5p1Im1drj8kuRKtCZnzBBazovUccnX"
access_token="933075473399246849-BUYqU5ioK2mbLCj7beGuOLkqPY7W0Fs"
access_token_secret="TUpB14OSRpJvKn9NPY8NwqLqdM6y2UYUEhocHx7obpXAM"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()

for tweet in public_tweets:
    print tweet.text
    print tweet.user.screen_name
