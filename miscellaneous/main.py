from . import textAndVoice
from aiogram import types, Dispatcher

def register_handlers_misc(dp: Dispatcher):
    dp.register_message_handler(textAndVoice.voice, commands=['voice'])
    dp.register_message_handler(textAndVoice.voiceAns, content_types=['voice'])
    dp.register_callback_query_handler(textAndVoice.acceptVoice, text=['acceptVoice_Ua', 'acceptVoice_Ru'])