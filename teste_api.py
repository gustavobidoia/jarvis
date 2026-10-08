import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

resposta = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="Explique em uma frase o que é uma variável em Python.",
)
print(resposta.text)