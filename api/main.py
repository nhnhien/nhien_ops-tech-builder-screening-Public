from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
from openai import OpenAI 
import logging
logging.basicConfig(level=logging.INFO)

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Get API key from environment variable
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def call_openai(text):
    # Mock summary data instead of calling the API
    return f"[OpenAI Summary - mock] Summary: {text[:60]}..."

def call_claude(text):
    # Mock Claude summary
    return f"[Claude Summary - mock] {text[:50]}..."

@app.route("/summarize", methods=["POST"])
def summarize():
    data = request.get_json()
    text = data.get("text", "")
    model = data.get("model", "openai")

    if not text:
        return jsonify({"error": "Missing text"}), 400

    try:
        if model == "claude":
            summary = call_claude(text)
        else:
            summary = call_openai(text)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    return jsonify({"summary": summary})

if __name__ == "__main__":
    app.run(debug=True)
