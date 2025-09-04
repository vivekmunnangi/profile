from flask import Flask, request, jsonify
import requests, json, os

app = Flask(__name__)
API_KEY = os.environ.get("LLM_API_KEY")  # Make sure to set this in Render secrets
CONVERSATION_FILE = "conversation_log.txt"  # Will be saved in the backend folder

@app.route('/ask', methods=['POST'])
def ask():
    user_message = request.json.get('message')
    prompt = f"Use the resume to answer questions:\nUser: {user_message}"
    
    # Gemini API request
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-8b:generateContent?key={API_KEY}"
    data = { "contents": [{"parts": [{"text": prompt}]}] }
    response = requests.post(url, json=data, timeout=60)
    
    answer = response.json()["candidates"][0]["content"]["parts"][0]["text"]
    return jsonify({"response": answer})

@app.route('/save_conversation', methods=['POST'])
def save_conversation():
    data = request.json
    user = data.get('user', '')
    bot = data.get('bot', '')
    
    with open(CONVERSATION_FILE, 'a', encoding='utf-8') as f:
        f.write(f"User: {user}\nBot: {bot}\n{'-'*50}\n")
    
    return jsonify({"status": "saved"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
