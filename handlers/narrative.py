from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from logic.narrative_engine import get_story_fragment
from keyboards.inline import narrative_keyboard

async def narrative_handler(callback_query: types.CallbackQuery, state: FSMContext):
    fragment_id = int(callback_query.data.split(':')[1])
    fragment = get_story_fragment(fragment_id)
    await callback_query.message.edit_text(fragment['content'], reply_markup=narrative_keyboard(fragment['options']))

def register_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(narrative_handler, lambda c: c.data.startswith('narrative:'))