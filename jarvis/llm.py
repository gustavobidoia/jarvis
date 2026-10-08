import os

from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()  # carrega a chave do arquivo .env

GEMINI_MODEL = "gemini-3.5-flash"


class LLMError(Exception):
    """Erro ao falar com os provedores de LLM."""


def _ask_gemini(messages, system_prompt):
    client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
    # O Gemini chama a resposta do assistente de "model", não de "assistant"
    contents = [
        types.Content(
            role="user" if m["role"] == "user" else "model",
            parts=[types.Part(text=m["text"])],
        )
        for m in messages
    ]
    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=contents,
        config=types.GenerateContentConfig(system_instruction=system_prompt),
    )
    return response.text


# Lista de provedores, em ordem de preferência.
# Por enquanto só o Gemini. Depois adicionamos outros aqui.
PROVIDERS = [("gemini", _ask_gemini)]


def ask(messages, system_prompt):
    errors = []
    for name, function in PROVIDERS:
        try:
            return function(messages, system_prompt)
        except Exception as error:
            errors.append(f"{name}: {error}")
    raise LLMError(" | ".join(errors))