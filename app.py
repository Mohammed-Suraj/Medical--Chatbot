from flask import Flask, render_template, request, jsonify, redirect, session
import os
from groq import Groq

app = Flask(__name__)
app.secret_key = "super_secret_key"   # you can change it

# ---- USE ENV VARIABLE (Render safe) ----
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

MODEL = "llama-3.1-8b-instant"


def ask_ai(message, lang):
    try:
        if lang == "en":
            prompt = (
                "You are a polite medical awareness assistant. "
                "Do NOT diagnose diseases. "
                "Explain in simple English, suggest prevention tips "
                "and when to see a doctor. "
                f"User: {message}"
            )
        else:
            prompt = (
                "நீங்கள் தமிழ் மருத்துவ விழிப்புணர்வு உதவியாளர். "
                "நோயை உறுதி செய்ய வேண்டாம். "
                "எளிய விளக்கம், தடுப்பு வழிகள், "
                "மருத்துவரை எப்போது பார்க்க வேண்டும் என்று சொல்லுங்கள். "
                f"பயனர்: {message}"
            )

        response = client.chat.completions.create(
            model=MODEL,
            messages=[{"role": "user", "content": prompt}]
        )

        return response.choices[0].message.content

    except Exception as e:
        print("SERVER ERROR:", e)
        return "Server problem. Check API key / internet."


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    reply = ask_ai(data["message"], data["lang"])
    return jsonify({"reply": reply})


# ---- Render Compatible Server Run ----
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
