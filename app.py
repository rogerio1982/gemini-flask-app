from flask import Flask, request, jsonify
import google.genai as genai
import os
import json

app = Flask(__name__)

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

@app.route("/")
def home():
    return {"message": "Flask + Gemini rodando na aws 🚀"}

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = json.loads(request.data.decode('utf-8', errors='ignore'))
        prompt = data.get("prompt")

        if not prompt:
            return jsonify({"error": "Prompt é obrigatório"}), 400

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )
        return jsonify({"response": response.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)