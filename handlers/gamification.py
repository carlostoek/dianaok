from aiogram import types, Dispatcher
from logic.gamification import process_user_action

async def gamification_handler(message: types.Message):
    user_id = message.from_user.id
    action = message.text  # Suponiendo que la acción es el texto del mensaje
    result = process_user_action(user_id, action)
    await message.answer(result)

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(gamification_handler, content_types=types.ContentType.TEXT)