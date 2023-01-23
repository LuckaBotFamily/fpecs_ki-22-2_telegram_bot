from . import textAndVoice
from aiogram import types, Dispatcher

def register_handlers_misc(dp: Dispatcher):
    dp.register_message_handler(textAndVoice.voice, commands=['voice'])