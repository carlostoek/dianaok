import pytest
from src.message_handler import MessageHandler

def test_handle_text_message():
    handler = MessageHandler()
    assert handler.handle_text_message("hola") == "¡Hola! ¿Cómo puedo ayudarte?"
    assert handler.handle_text_message("adios") == "Lo siento, no entiendo el mensaje."