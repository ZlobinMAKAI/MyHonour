from aiogram.dispatcher.filters.state import StatesGroup, State


class Mail(StatesGroup):
    mail = State()


class Read(StatesGroup):
    reading = State()


class Upload(StatesGroup):
    uploading = State()
