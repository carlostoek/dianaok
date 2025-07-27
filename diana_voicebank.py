def get_phrase(context):
    phrases = {
        "welcome": "Bienvenido a este mundo de misterio y aventura.",
        "farewell": "Hasta pronto, valiente explorador.",
        "curious": "La curiosidad es el primer paso hacia el conocimiento.",
        "playful": "La vida es un juego, y tú eres el protagonista.",
        "melancholic": "A veces, el silencio dice más que mil palabras."
    }
    return phrases.get(context, "Frase no encontrada.")