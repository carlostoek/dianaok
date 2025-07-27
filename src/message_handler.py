class MessageHandler:
    def handle_text_message(self, message: str) -> str:
        # Procesa el mensaje de texto y devuelve una respuesta
        if message.lower() == "hola":
            return "¡Hola! ¿Cómo puedo ayudarte?"
        else:
            return "Lo siento, no entiendo el mensaje."