from flask import Flask, render_template, request, jsonify
from groq import Groq

app = Flask(__name__)

client = Groq(api_key="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")

MODEL = "llama-3.1-8b-instant"

def ask_ai(message, lang):
    try:
        if lang == "en":
            prompt = (
                "You are a polite medical awareness assistant. "
                "Do NOT diagnose diseases. "
                "Explain in simple English, suggest prevention, "
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


if __name__ == "__main__":
    app.run(debug=True)
