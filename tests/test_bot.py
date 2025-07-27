import pytest
from src.bot import Bot

def test_process_message():
    bot = Bot()
    assert bot.process_message("hola") == "¡Hola! ¿Cómo puedo ayudarte?"
    assert bot.process_message("adios") == "Lo siento, no entiendo el mensaje."