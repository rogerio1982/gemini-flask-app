from flask import Flask, request, jsonify
import google.genai as genai
import os

app = Flask(__name__)

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

@app.route("/")
def home():
    return {"message": "Flask + Gemini rodando 🚀"}

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    prompt = data.get("prompt")

    if not prompt:
        return jsonify({"error": "Prompt é obrigatório"}), 400

    response = client.models.generate_content(model="gemini-1.5-flash", contents=prompt)
    return jsonify({"response": response.text})
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)