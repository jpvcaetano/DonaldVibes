import json
import os
import time

from config import *
from logger_config import setup_logger
from mood_analyzer import MoodAnalyzer
from twitter_handler import TwitterHandler

logger = setup_logger("main")


def main():
    logger.info("Starting Tweet Mood Analyzer Bot")

    # Initialize handlers
    twitter = TwitterHandler(
        TWITTER_API_KEY,
        TWITTER_API_SECRET,
        TWITTER_ACCESS_TOKEN,
        TWITTER_ACCESS_TOKEN_SECRET,
        TWITTER_BEARER_TOKEN,
    )

    mood_analyzer = MoodAnalyzer(OPENAI_API_KEY)

    # Load previously processed tweet IDs from file
    processed_tweets_file = "processed_tweets.json"
    processed_tweets = set()
    if not os.path.exists(processed_tweets_file):
        with open(processed_tweets_file, "w") as f:
            json.dump(list(processed_tweets), f)
            logger.info("Created new processed tweets file")
    else:
        with open(processed_tweets_file, "r") as f:
            processed_tweets = set(json.load(f))
            logger.info(f"Loaded {len(processed_tweets)} processed tweet IDs")

    while True:
        try:
            # Get latest tweet
            latest_tweet = twitter.get_latest_tweet(TARGET_ACCOUNT)

            if latest_tweet and str(latest_tweet.id) not in processed_tweets:
                logger.info(f"New tweet found from {TARGET_ACCOUNT}")

                # Save updated processed tweets to file
                with open(processed_tweets_file, "w") as f:
                    json.dump(list(processed_tweets), f)

                # Analyze mood and post response
                mood = mood_analyzer.analyze_mood(latest_tweet.text)
                response_text = f"I am feeling {mood}."
                twitter.post_tweet(response_text)

                # New tweet processed
                processed_tweets.add(str(latest_tweet.id))
                with open(processed_tweets_file, "w") as f:
                    json.dump(list(processed_tweets), f)

                logger.info(f"Processed tweet: {latest_tweet.text}")
                logger.info(f"Detected mood: {mood}")
            else:
                logger.debug("No new tweets found")

            # Wait for next check
            logger.debug(f"Waiting {CHECK_INTERVAL} minutes before next check")
            time.sleep(CHECK_INTERVAL * 60)

        except Exception as e:
            logger.error(f"Error in main loop: {e}", exc_info=True)
            time.sleep(60)  # Wait a minute before retrying


if __name__ == "__main__":
    main()
