from twitter_handler import TwitterHandler
from mood_analyzer import MoodAnalyzer
from config import *
import time
import json
import os

def main():
    # Initialize handlers
    twitter = TwitterHandler(
        TWITTER_API_KEY,
        TWITTER_API_SECRET,
        TWITTER_ACCESS_TOKEN,
        TWITTER_ACCESS_TOKEN_SECRET
    )
    
    mood_analyzer = MoodAnalyzer(OPENAI_API_KEY)
    
    # Keep track of last processed tweet
    last_tweet_id = None
    
    while True:
        try:
            # Get latest tweet
            latest_tweet = twitter.get_latest_tweet(TARGET_ACCOUNT)
            
            if latest_tweet and (not last_tweet_id or latest_tweet.id != last_tweet_id):
                # New tweet found
                last_tweet_id = latest_tweet.id
                
                # Analyze mood
                mood = mood_analyzer.analyze_mood(latest_tweet.text)
                
                # Create and post response
                response_text = f"@{TARGET_ACCOUNT}'s latest tweet seems {mood}��"
                twitter.post_tweet(response_text)
                
                print(f"Processed tweet: {latest_tweet.text}")
                print(f"Detected mood: {mood}")
            
            # Wait for next check
            time.sleep(CHECK_INTERVAL * 60)
            
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(60)  # Wait a minute before retrying

if __name__ == "__main__":
    main() 