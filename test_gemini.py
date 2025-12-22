from google import genai

client = genai.Client(api_key="YOUR_API_KEY")

res = client.models.generate_content(
    model="gemini-1.5-flash",
    contents="Say hello"
)

print(res.text)
