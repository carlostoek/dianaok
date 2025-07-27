from aiogram import types, Dispatcher
from database.queries import add_reaction
from database.setup import SessionLocal

async def reaction_handler(message: types.Message):
    db = SessionLocal()
    user_id = message.from_user.id
    message_id = message.message_id
    emoji = message.text  # Suponiendo que el emoji es el texto del mensaje
    add_reaction(db, user_id, message_id, emoji)
    await message.answer("Reacción registrada.")
    db.close()

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(reaction_handler, content_types=types.ContentType.TEXT)