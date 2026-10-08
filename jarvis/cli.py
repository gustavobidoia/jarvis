from jarvis.core import Assistant


def main():
    assistant = Assistant()
    print("JARVIS pronto. Digite 'sair' para encerrar.")
    while True:
        try:
            text = input("Você: ").strip()
        except (KeyboardInterrupt, EOFError):  # Ctrl+C ou Ctrl+Z
            print("\nAté logo!")
            break
        if not text:
            continue
        if text.lower() in ("sair", "exit"):
            print("Até logo!")
            break
        print(f"JARVIS: {assistant.handle_message(text)}")