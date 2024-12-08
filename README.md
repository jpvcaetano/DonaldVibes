 # Twitter Mood Analyzer Bot

A Python bot that monitors a Twitter/X account, analyzes tweet moods using GPT-4, and posts the results.

## Features

- Real-time Twitter account monitoring
- GPT-4 powered mood analysis
- Automatic mood response tweets
- Duplicate tweet prevention
- Comprehensive logging system
- Error handling and automatic retries

## Requirements

- Python 3.8+
- Twitter/X Developer Account with API access (including Bearer Token)
- OpenAI API key

## Quick Start

1. Clone and install dependencies:
```bash
git clone <repository-url>
cd twitter-mood-analyzer
pip install tweepy openai python-dotenv httpx
```

2. Set up environment:

```bash
cp .env.example .env
```

3. Run the bot:
```bash
python main.py
```

## Environment Variables

Required in your `.env` file:
```bash
TWITTER_API_KEY=your_api_key
TWITTER_API_SECRET=your_api_secret
TWITTER_ACCESS_TOKEN=your_access_token
TWITTER_ACCESS_TOKEN_SECRET=your_access_token_secret
TWITTER_BEARER_TOKEN=your_bearer_token
OPENAI_API_KEY=your_openai_api_key
```


## Project Structure

- `main.py`: Bot's main execution loop
- `twitter_handler.py`: Twitter API integration
- `mood_analyzer.py`: OpenAI GPT-4 integration
- `config.py`: Configuration management
- `logger_config.py`: Logging setup

## Logging

- Console and file output
- Rotating log files (1MB each, 5 backups)
- Logs stored in `bot.log`

## Error Handling

- API authentication verification
- Automatic retries on failure
- Detailed error logging
- Persistent tweet tracking

## Security Notes

- Never commit `.env` file
- Secure your API credentials
- Monitor API usage costs
- SSL verification is disabled for OpenAI calls

## Troubleshooting

Check `bot.log` for detailed error messages and verify:
- Environment variables are set correctly
- Twitter Developer Account access level
- API rate limits
- Internet connectivity

## License

[Your License Here]