import tweepy
from auth_keys import consumer_key, consumer_secret, token, token_secret


# Handling authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

# Set tokens
auth.set_access_token(token, token_secret)

# Instantiate object with all methods to access Twitter API
api = tweepy.API(auth)
