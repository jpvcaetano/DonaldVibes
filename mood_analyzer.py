import httpx
from openai import OpenAI

from logger_config import setup_logger

logger = setup_logger("mood_analyzer")


class MoodAnalyzer:
    def __init__(self, api_key):
        self.client = OpenAI(api_key=api_key, http_client=httpx.Client(verify=False))
        logger.info("Mood analyzer initialized successfully")

    def analyze_mood(self, tweet_text):
        prompt = f"""Analyze the mood of the following tweet and respond with a single word 
        (happy, sad, angry, excited, neutral, etc.): "{tweet_text}" """
        messages = [
            {"role": "system", "content": "You are a mood analysis assistant."},
            {"role": "user", "content": prompt},
        ]
        try:
            response = self.client.chat.completions.create(
                model="gpt-4o", messages=messages, temperature=0.2, max_tokens=100
            )
            mood = response.choices[0].message.content.strip().lower()
            logger.info(f"Successfully analyzed mood: {mood}")
            return mood
        except Exception as e:
            logger.error(f"Error analyzing mood: {e}")
            raise
