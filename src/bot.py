from src.message_handler import MessageHandler

class Bot:
    def __init__(self):
        self.message_handler = MessageHandler()

    def start(self):
        print("Bot started. Listening for messages...")

    def process_message(self, message: str) -> str:
        return self.message_handler.handle_text_message(message)