import os

import tweepy

consumer_key = os.getenv('SOCIAL_AUTH_TWITTER_KEY')
consumer_secret = os.getenv('SOCIAL_AUTH_TWITTER_SECRET')

def get_twitter_api(oauth_token, oauth_token_secret):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(oauth_token, oauth_token_secret)
    return tweepy.API(auth)