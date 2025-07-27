from aiogram.dispatcher.filters.state import State, StatesGroup

class UserStates(StatesGroup):
    NARRATIVE = State()
    STORE = State()