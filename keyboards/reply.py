from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def main_menu_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton("Narrativa"))
    keyboard.add(KeyboardButton("Tienda"))
    return keyboard