import json
import os
from datetime import datetime, timezone

import tweepy

from logger_config import setup_logger

logger = setup_logger("twitter_handler")


class TwitterHandler:
    def __init__(
        self, api_key, api_secret, access_token, access_token_secret, bearer_token
    ):
        auth = tweepy.OAuthHandler(api_key, api_secret)
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)
        self.client = tweepy.Client(
            consumer_key=api_key,
            consumer_secret=api_secret,
            access_token=access_token,
            access_token_secret=access_token_secret,
            bearer_token=bearer_token,
        )
        logger.info("Twitter handler initialized successfully")

    def get_latest_tweet(self, username):
        tweets = self.client.get_users_tweets(
            self.get_user_id(username), max_results=5, tweet_fields=["created_at"]
        )
        if not tweets.data:
            logger.warning(f"No tweets found for user {username}")
            return None
        logger.info(f"Retrieved latest tweet from {username}")
        return tweets.data[0]

    def get_user_id(self, username):
        try:
            user = self.client.get_user(username=username)
            logger.info(f"Retrieved user ID for {username}")
            return user.data.id
        except Exception as e:
            logger.error(f"Failed to get user ID for {username}: {e}")
            raise

    def post_tweet(self, text):
        try:
            self.client.create_tweet(text=text)
            logger.info(f"Successfully posted tweet: {text}")
            return True
        except Exception as e:
            logger.error(f"Error posting tweet: {e}")
            return False
