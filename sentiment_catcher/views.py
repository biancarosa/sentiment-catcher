import os

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from sentiment_catcher.helpers import social_auth, twitter_api

@login_required
def home(request):
    oauth_token, oauth_token_secret = social_auth.get_oauth_tokens(request.user)

    api = twitter_api.get_twitter_api(oauth_token, oauth_token_secret)

    tweets = []
    for tweet in api.user_timeline(count=100,
        tweet_mode='extended', include_rts=False, 
        exclude_replies=True):
        tweets.append(tweet.full_text)
    ctx = {
        'user': request.user,
        'tweets': tweets
    }
    return render(request, 'sentiment_catcher/home.html', ctx)
