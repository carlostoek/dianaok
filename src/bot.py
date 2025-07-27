from aiogram import Dispatcher, types

def register_handlers(dp: Dispatcher):
    @dp.message_handler(commands=['start', 'help'])
    async def send_welcome(message: types.Message):
        await message.reply("Hello! I'm your bot. How can I assist you today?")