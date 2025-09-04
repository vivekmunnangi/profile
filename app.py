from flask import Flask, request, jsonify
import requests, os
import pdfplumber
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

# Get API key from Render environment
API_KEY = os.environ.get("LLM_API_KEY")  
CONVERSATION_FILE = "conversation_log.txt"  # Save conversations here
RESUME_FILE = "resume.pdf"  # Your resume in same folder

# Extract resume text once at startup
resume_text = ""
with pdfplumber.open(RESUME_FILE) as pdf:
    for page in pdf.pages:
        resume_text += page.extract_text() + "\n"

@app.route('/ask', methods=['POST'])
def ask():
    user_message = request.json.get('message')
    
    # Combine resume and user question into prompt
    prompt = f"Your are a good chat assistant, with your skills can you answer the question related to me based on my resume(do not share by phone number, if asked reply that due to security reasons that is not possible):\n{resume_text}\n\nUser Question: {user_message}"

    # Gemini API request
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-8b:generateContent?key={API_KEY}"
    data = { "contents": [{"parts": [{"text": prompt}]}] }
    
    try:
        response = requests.post(url, json=data, timeout=60)
        response.raise_for_status()
        answer = response.json()["candidates"][0]["content"]["parts"][0]["text"]
    except Exception as e:
        answer = f"Error fetching response: {str(e)}"

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
