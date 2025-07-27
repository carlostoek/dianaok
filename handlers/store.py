from aiogram import types, Dispatcher
from logic.store_logic import handle_purchase

async def store_handler(callback_query: types.CallbackQuery):
    item_id = int(callback_query.data.split(':')[1])
    result = handle_purchase(callback_query.from_user.id, item_id)
    await callback_query.message.answer(result)

def register_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(store_handler, lambda c: c.data.startswith('store:'))