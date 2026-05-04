import os
import json
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from dotenv import load_dotenv
import openai
from datetime import datetime
import sqlite3

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)
CORS(app)
limiter = Limiter(
    app=app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)

# Conversation history storage
conversations = {}

def init_db():
    conn = sqlite3.connect('chatbot.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS conversations
                 (id TEXT PRIMARY KEY, user_id TEXT, timestamp TEXT, role TEXT, content TEXT)''')
    conn.commit()
    conn.close()

init_db()

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok", "backend": "python"}), 200

@app.route('/chat', methods=['POST'])
@limiter.limit("10 per minute")
def chat():
    """Handle text-based chat requests"""
    try:
        data = request.json
        user_message = data.get('message')
        user_id = data.get('user_id', 'default')
        
        if not user_message:
            return jsonify({"error": "Message is required"}), 400
        
        if user_id not in conversations:
            conversations[user_id] = []
        
        conversations[user_id].append({
            "role": "user",
            "content": user_message
        })
        
        system_prompt = {
            "role": "system",
            "content": "You are a helpful, friendly AI assistant. Provide clear, concise responses."
        }
        
        messages = [system_prompt] + conversations[user_id][-10:]
        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.7,
            max_tokens=500
        )
        
        bot_response = response.choices[0].message.content
        
        conversations[user_id].append({
            "role": "assistant",
            "content": bot_response
        })
        
        save_to_db(user_id, "user", user_message)
        save_to_db(user_id, "assistant", bot_response)
        
        return jsonify({
            "reply": bot_response,
            "timestamp": datetime.now().isoformat()
        }), 200
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/history/<user_id>', methods=['GET'])
@limiter.limit("5 per minute")
def get_history(user_id):
    try:
        if user_id in conversations:
            return jsonify({"history": conversations[user_id]}), 200
        return jsonify({"history": []}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/clear/<user_id>', methods=['POST'])
@limiter.limit("5 per minute")
def clear_history(user_id):
    try:
        if user_id in conversations:
            conversations[user_id] = []
        return jsonify({"message": "History cleared"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def save_to_db(user_id, role, content):
    try:
        conn = sqlite3.connect('chatbot.db')
        c = conn.cursor()
        c.execute("INSERT INTO conversations VALUES (?, ?, ?, ?, ?)",
                  (f"{user_id}_{datetime.now().timestamp()}", user_id, datetime.now().isoformat(), role, content))
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"DB Error: {e}")

@app.errorhandler(429)
def ratelimit_handler(e):
    return jsonify({"error": "Rate limit exceeded"}), 429

if __name__ == "__main__":
    app.run(debug=True, port=5000)