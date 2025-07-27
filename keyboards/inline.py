from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def narrative_keyboard(options):
    keyboard = InlineKeyboardMarkup()
    for option in options:
        keyboard.add(InlineKeyboardButton(option['text'], callback_data=f"narrative:{option['id']}"))
    return keyboard