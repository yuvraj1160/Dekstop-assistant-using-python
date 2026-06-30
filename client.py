from google import genai

CLIENT_API_KEY = "Use your API key here"

# 2. Naya Client initialize karein
client = genai.Client(api_key=CLIENT_API_KEY)

# 3. Model ko call karein (Naya SDK automatically latest model route kar leta hai)
response = client.models.generate_content(
    model="gemini-2.5-flash", # Ya bas 'gemini-2.0-flash'
    contents="coding kya hoti hai.",
)

# 4. Response print karein
print("Assistant:", response.text)

