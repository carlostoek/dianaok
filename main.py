import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import ParseMode
from aiogram.utils import executor
from utils.config import load_config
from handlers import start, narrative, reactions, gamification, store, admin_panel

# Configurar el logging
logging.basicConfig(level=logging.INFO)

# Cargar configuración
config = load_config()

# Inicializar bot y dispatcher
bot = Bot(token=config.bot_token, parse_mode=ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# Registrar handlers
start.register_handlers(dp)
narrative.register_handlers(dp)
reactions.register_handlers(dp)
gamification.register_handlers(dp)
store.register_handlers(dp)
admin_panel.register_handlers(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)