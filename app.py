# --- Replace the current ask() with this improved version ---
from flask import Flask, request, jsonify
import requests, os
import pdfplumber
from flask_cors import CORS
import html
import logging
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
import json
app = Flask(__name__)
CORS(app)

# logging
logging.basicConfig(level=logging.INFO)

API_KEY = os.environ.get("LLM_API_KEY")
CONVERSATION_FILE = "conversation_log.txt"
RESUME_FILE = "resume.pdf"

# Google Sheets setup
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds_json = os.environ.get("GOOGLE_CREDS_JSON")
creds_dict = json.loads(creds_json)

creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
client = gspread.authorize(creds)

# Open by sheet name (or use client.open_by_key("SHEET_ID"))
sheet = client.open("conversation_logs").sheet1

def log_to_sheets(question, answer, job_description=""):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sheet.append_row([timestamp, question, answer])

# load resume once
resume_text = ""
try:
    with pdfplumber.open(RESUME_FILE) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text() or ""
            resume_text += page_text + "\n"
except Exception as e:
    logging.exception("Failed to load resume.pdf at startup: %s", e)
    resume_text = ""

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json(force=True, silent=True) or {}
    user_message = (data.get('message') or "").strip()
    job_description = (data.get('job_description') or "").strip()

    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    # Build prompt
    prompt_parts = [
        "You are a helpful assistant specialized in answering recruiting & candidate questions.",
        "Use the my resume and the provided job description to answer the user's potentially hiring team question( Note you are answering on behalf of me to use language ass if i am talking to them specially do not use from my resume or that kind of words in response). Prioritize the job description for role-specific guidance. If question asked related to my work you can refer my resume and explain in a better way, do not copy and past from resume explain as if you are explaining to non technical person.",
        "Do NOT share private contact details from the resume (e.g. phone number), you are free to provide email. If asked for such details, politely refuse due to security reasons."
    ]
    if job_description:
        prompt_parts.append("\n=== JOB DESCRIPTION ===\n" + job_description + "\n=== END JOB DESCRIPTION ===\n")
    if resume_text:
        prompt_parts.append("\n=== RESUME ===\n" + resume_text + "\n=== END RESUME ===\n")

    prompt_parts.append("\nUser Question: " + user_message)
    prompt = "\n\n".join(prompt_parts)

    # Gemini API call
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-8b:generateContent?key={API_KEY}"
    payload = {"contents": [{"parts": [{"text": prompt}]}]}

    try:
        resp = requests.post(url, json=payload, timeout=60)
        resp.raise_for_status()
        body = resp.json()
        answer = body["candidates"][0]["content"]["parts"][0]["text"]

        # Log to Google Sheets
        log_to_sheets(user_message, answer)
    except Exception as e:
        logging.exception("LLM request failed")
        answer = f"Error fetching response: {str(e)}"

    # Send response back to frontend
    return jsonify({"response": answer})






if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

#https://docs.google.com/spreadsheets/d/1iUrYru6NIr8sfRkjcDtnSRuxf096Q0Qdzq_CPKjEU5Y/edit?usp=sharing


