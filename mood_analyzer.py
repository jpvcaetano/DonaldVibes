import openai
from logger_config import setup_logger

logger = setup_logger('mood_analyzer')

class MoodAnalyzer:
    def __init__(self, api_key):
        openai.api_key = api_key
        logger.info("Mood analyzer initialized successfully")

    def analyze_mood(self, tweet_text):
        prompt = f"""Analyze the mood of the following tweet and respond with a single word 
        (happy, sad, angry, excited, neutral, etc.): "{tweet_text}" """
        
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "You are a mood analysis assistant."},
                    {"role": "user", "content": prompt}
                ]
            )
            mood = response.choices[0].message.content.strip().lower()
            logger.info(f"Successfully analyzed mood: {mood}")
            return mood
        except Exception as e:
            logger.error(f"Error analyzing mood: {e}")
            raise 