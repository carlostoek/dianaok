from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from database.queries import get_user, create_user
from database.setup import SessionLocal

async def start_command(message: types.Message, state: FSMContext):
    db = SessionLocal()
    user = get_user(db, message.from_user.id)
    if not user:
        user = create_user(db, message.from_user.id, message.from_user.username)
    await message.answer(f"Bienvenido, {user.username}! Soy Diana, tu guía en esta aventura.")
    db.close()

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_command, Command("start"))