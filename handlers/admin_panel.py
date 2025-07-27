from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Command
from logic.access_control import is_admin

async def admin_command(message: types.Message):
    if is_admin(message.from_user.id):
        await message.answer("Bienvenido al panel administrativo.")
    else:
        await message.answer("No tienes permiso para acceder a esta función.")

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(admin_command, Command("admin"))