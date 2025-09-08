# --- Replace the current ask() with this improved version ---
from flask import Flask, request, jsonify
import requests, os
import pdfplumber
from flask_cors import CORS
import html
import logging

app = Flask(__name__)
CORS(app)

# logging
logging.basicConfig(level=logging.INFO)

API_KEY = os.environ.get("LLM_API_KEY")
CONVERSATION_FILE = "conversation_log.txt"
RESUME_FILE = "resume.pdf"

# constants
JOB_DESC_MAX = 6000  # max number of characters of job description to include (adjust if needed)

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
    """
    Expects JSON { "message": "...", "job_description": "..." (optional) }
    """
    data = request.get_json(force=True, silent=True) or {}
    user_message = (data.get('message') or "").strip()
    job_description = (data.get('job_description') or "").strip()

    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    # Truncate job_description to avoid extremely large payloads
    if len(job_description) > JOB_DESC_MAX:
        job_description = job_description[:JOB_DESC_MAX]
        logging.info("Job description truncated to %d chars", JOB_DESC_MAX)

    # Build a clear prompt: prioritize the job description (if present) and the resume
    # Keep instructions short and explicit about privacy (already in your code)
    prompt_parts = [
        "You are a helpful assistant specialized in answering recruiting & candidate questions.",
        "Use the my resume and the provided job description to answer the user's potentially hiring team question( Note you are answering on behalf of me to use language ass if i am talking to them specially do not use from my resume or that kind of words in response). Prioritize the job description for role-specific guidance. If question asked related to my work you can refer my resume and explain in a better way, do not copy and past from resume explain as if you are explaining to non technical person.",
        "Do NOT share private contact details from the resume (e.g. phone number), you are free to provide email. If asked for such details, politely refuse due to security reasons."
    ]

    if job_description:
        prompt_parts.append("\n=== JOB DESCRIPTION ===\n" + job_description + "\n=== END JOB DESCRIPTION ===\n")
    if resume_text:
        # Keep resume text but if it's huge you could consider truncating similarly
        prompt_parts.append("\n=== RESUME ===\n" + resume_text + "\n=== END RESUME ===\n")

    prompt_parts.append("\nUser Question: " + user_message)
    prompt = "\n\n".join(prompt_parts)

    # Prepare Gemini request (same as before)
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-8b:generateContent?key={API_KEY}"
    payload = {"contents": [{"parts": [{"text": prompt}]}]}

    try:
        resp = requests.post(url, json=payload, timeout=60)
        resp.raise_for_status()
        body = resp.json()
        answer = body["candidates"][0]["content"]["parts"][0]["text"]
    except Exception as e:
        logging.exception("LLM request failed")
        answer = f"Error fetching response: {str(e)}"
    finally:
    # Write to log file regardless of success/failure
        try:
            with open("conversation_log.txt", "a", encoding="utf-8") as f:
                f.write("User Prompt:\n")
                f.write(prompt + "\n\n")
                f.write("Assistant Answer / Error:\n")
                f.write(answer + "\n")
                f.write("-" * 60 + "\n")
        except Exception as log_err:
            logging.exception("Failed to write log file")

    # Save conversation to disk (including job description for traceability)
    try:
        with open(CONVERSATION_FILE, "a", encoding="utf-8") as f:
            f.write("User Question:\n")
            f.write(user_message + "\n\n")
            if job_description:
                f.write("Job Description (truncated):\n")
                f.write(job_description + "\n\n")
            if resume_text:
                f.write("Resume (excerpt):\n")
                f.write((resume_text[:2000] + "\n\n") if len(resume_text) > 2000 else (resume_text + "\n\n"))
            f.write("Assistant Answer:\n")
            f.write(answer + "\n")
            f.write("-" * 60 + "\n")
    except Exception as e:
        logging.exception("Failed to save conversation")

    return jsonify({"response": answer})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

