from jarvis import llm

SYSTEM_PROMPT = (
    "Você é o JARVIS, assistente pessoal do Gustavo. "
    "Responda sempre em português do Brasil, de forma direta e objetiva. "
    "Se não souber algo, diga que não sabe em vez de inventar."
)

# Quantas mensagens do histórico enviar ao modelo. Ímpar de propósito:
# assim o trecho enviado sempre começa com uma mensagem do usuário.
MAX_HISTORY = 21


class Assistant:
    def __init__(self):
        self.history = []

    def handle_message(self, text):
        self.history.append({"role": "user", "text": text})
        try:
            answer = llm.ask(self.history[-MAX_HISTORY:], SYSTEM_PROMPT)
        except llm.LLMError as error:
            self.history.pop()  # remove a pergunta que ficou sem resposta
            return f"Não consegui falar com o modelo: {error}"
        self.history.append({"role": "assistant", "text": answer})
        return answer