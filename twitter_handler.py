import tweepy
from datetime import datetime, timezone
import json
import os

class TwitterHandler:
    def __init__(self, api_key, api_secret, access_token, access_token_secret):
        auth = tweepy.OAuthHandler(api_key, api_secret)
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)
        self.client = tweepy.Client(
            consumer_key=api_key,
            consumer_secret=api_secret,
            access_token=access_token,
            access_token_secret=access_token_secret
        )
        
    def get_latest_tweet(self, username):
        tweets = self.client.get_users_tweets(
            self.get_user_id(username),
            max_results=5,
            tweet_fields=['created_at']
        )
        if not tweets.data:
            return None
        return tweets.data[0]
    
    def get_user_id(self, username):
        user = self.client.get_user(username=username)
        return user.data.id
    
    def post_tweet(self, text):
        try:
            self.client.create_tweet(text=text)
            return True
        except Exception as e:
            print(f"Error posting tweet: {e}")
            return False 