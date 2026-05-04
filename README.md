# AI-Powered Chatbot with Voice Assistant

A full-stack AI chatbot with voice input/output, conversation history, and dual backend support (Python & Node.js).

## Features
✅ Text-based chat with OpenAI GPT-4
✅ Voice input (Speech-to-Text)
✅ Voice output (Text-to-Speech)
✅ Conversation history & context
✅ Dual backends (Python + Node.js)
✅ Modern responsive UI
✅ Rate limiting & security
✅ Docker support

## Tech Stack
- **Frontend**: HTML5, CSS3, JavaScript (Web Speech API)
- **Backend (Python)**: Flask, OpenAI API
- **Backend (Node.js)**: Express.js, OpenAI API
- **Database**: SQLite (optional)
- **Deployment**: Docker, Render, Railway

## Quick Start

### Prerequisites
- Node.js 18+
- Python 3.8+
- OpenAI API key from https://platform.openai.com

### Setup Python Backend
```bash
cd backend-python
pip install -r requirements.txt
echo "OPENAI_API_KEY=your_api_key_here" > .env
python app.py
```

Server runs on: http://localhost:5000

### Setup Node.js Backend
```bash
cd backend-node
npm install
echo "OPENAI_API_KEY=your_api_key_here" > .env
npm start
```

Server runs on: http://localhost:5001

### Run Frontend
```bash
cd frontend
python -m http.server 8000
# or
npx http-server
```

Open: http://localhost:8000 (or your server port)

## API Endpoints

### Chat (Text)
**POST** `/chat`
```json
{
  "message": "Hello, AI!",
  "user_id": "user123"
}
```

Response:
```json
{
  "reply": "Hello! How can I help you today?",
  "timestamp": "2026-05-04T10:30:00Z"
}
```

### Get Conversation History
**GET** `/history/:user_id`

Response:
```json
{
  "history": [
    {"role": "user", "content": "Hello"},
    {"role": "assistant", "content": "Hi there!"}
  ]
}
```

### Clear History
**POST** `/clear/:user_id`

Response:
```json
{"message": "History cleared"}
```

### Voice Input (Node.js only)
**POST** `/voice`
```json
{
  "audio_base64": "...base64 encoded audio..."
}
```

## Docker Setup

### Run All Services
```bash
docker-compose up --build
```

This starts:
- Python backend: http://localhost:5000
- Node.js backend: http://localhost:5001
- Frontend: http://localhost:8080

### Run Individual Services
```bash
# Python only
docker build -t ai-chatbot-python ./backend-python
docker run -p 5000:5000 -e OPENAI_API_KEY=your_key ai-chatbot-python

# Node.js only
docker build -t ai-chatbot-node ./backend-node
docker run -p 5001:5001 -e OPENAI_API_KEY=your_key ai-chatbot-node
```

## Project Structure

```
ai-chatbot/
├── backend-python/
│   ├── app.py                 # Flask backend
│   ├── requirements.txt        # Python dependencies
│   ├── .env.example           # Environment template
│   └── Dockerfile             # Docker configuration
│
├── backend-node/
│   ├── server.js              # Express.js backend
│   ├── package.json           # Node dependencies
│   ├── .env.example           # Environment template
│   └── Dockerfile             # Docker configuration
│
├── frontend/
│   ├── index.html             # Web interface
│   ├── style.css              # Styling
│   └── script.js              # JavaScript logic
│
├── docker-compose.yml         # Multi-container setup
├── README.md                  # This file
├── CONTRIBUTING.md            # Contribution guidelines
└── .gitignore                # Git ignore rules
```

## Usage Guide

### Text Chat
1. Type your message in the input field
2. Press Enter or click "Send" button
3. Wait for AI response

### Voice Input
1. Click the 🎤 (microphone) button
2. Speak your question
3. Wait for transcription
4. Message appears in chat

### Voice Output
1. Send a message or wait for response
2. Click 🔊 (speaker) button
3. AI reads the last response aloud

### Clear Chat
1. Click "Clear History" button
2. All conversation history is deleted
3. Chat resets to welcome screen

## Configuration

### Environment Variables

**OPENAI_API_KEY** (Required)
- Your OpenAI API key
- Get it from: https://platform.openai.com/api-keys

**FLASK_ENV** (Python only)
- `development` or `production`
- Default: `development`

**NODE_ENV** (Node.js only)
- `development` or `production`
- Default: `development`

**PORT** (Node.js only)
- Server port
- Default: `5001`

### Custom System Prompt

Edit the system prompt in:
- Python: `backend-python/app.py` line ~70
- Node.js: `backend-node/server.js` line ~65

```python
system_prompt = {
    "role": "system",
    "content": "You are a helpful AI assistant specialized in Python programming."
}
```

## Security

⚠️ **Important Security Notes:**
- Never expose your API key in frontend code
- Always use environment variables for sensitive data
- Implement rate limiting (already included)
- Validate user input on backend
- Use HTTPS in production
- Monitor API usage and costs

### Rate Limits
- Chat: 10 requests per minute per IP
- History: 5 requests per minute per IP
- Voice: 10 requests per minute per IP

## Deployment

### Render.com
1. Push to GitHub
2. Connect repo to Render
3. Set environment variables
4. Deploy

### Railway.app
1. Connect GitHub account
2. Import project
3. Add environment variables
4. Deploy

### Heroku
1. `heroku create ai-chatbot`
2. `heroku config:set OPENAI_API_KEY=your_key`
3. `git push heroku main`

## Troubleshooting

### "Rate limit exceeded" error
- Wait a few minutes before making new requests
- Use `gpt-3.5-turbo` instead of `gpt-4` for cheaper option

### Voice input not working
- Check browser supports Web Speech API (Chrome, Edge, Safari)
- Allow microphone permissions
- Check internet connection

### API connection failed
- Verify OPENAI_API_KEY is set correctly
- Check API key hasn't expired
- Verify you have API credits

### Database errors
- Delete `chatbot.db` file to reset
- Check file permissions
- Ensure write access to directory

## Advanced Features

### Conversation Memory
Keeps last 10 messages for context in each conversation.

### Multiple Users
Each user gets their own conversation history using `user_id`.

### SQLite Persistence
All conversations are saved to `chatbot.db` for later retrieval.

### Custom Personalities
Modify system prompts to create specialized bots:
- Python tutor
- Customer support bot
- Content writer
- Code reviewer

## Performance Tips

- Use `gpt-3.5-turbo` for faster, cheaper responses
- Reduce `max_tokens` for shorter responses
- Cache common questions
- Implement pagination for large histories

## Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

MIT License - see LICENSE file for details

## Support

- 📖 [Documentation](README.md)
- 🐛 [Report Issues](https://github.com/neethuravi2007/ai-chatbot/issues)
- 💬 [Discussions](https://github.com/neethuravi2007/ai-chatbot/discussions)

## Roadmap

- [ ] Web interface improvements
- [ ] Multi-language support
- [ ] User authentication
- [ ] Payment integration
- [ ] Analytics dashboard
- [ ] Custom training data
- [ ] Slack integration
- [ ] Discord bot

## Credits

Built with ❤️ by Neeth Uravi

## Acknowledgments

- OpenAI for GPT API
- Flask and Express.js communities
- Web Speech API documentation
