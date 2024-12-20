import os

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Twitter/X API credentials
TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET")
TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
TWITTER_BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")

# OpenAI API credentials
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Target account to monitor (without @)
TARGET_ACCOUNT = "realDonaldTrump"

# How often to check for new tweets (in minutes)
CHECK_INTERVAL = 60
