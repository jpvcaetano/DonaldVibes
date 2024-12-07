import openai

class MoodAnalyzer:
    def __init__(self, api_key):
        openai.api_key = api_key

    def analyze_mood(self, tweet_text):
        prompt = f"""Analyze the mood of the following tweet and respond with a single word 
        (happy, sad, angry, excited, neutral, etc.): "{tweet_text}" """
        
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a mood analyzer. Respond with a single word describing the mood."},
                {"role": "user", "content": prompt}
            ]
        )
        
        return response.choices[0].message.content.strip().lower() 