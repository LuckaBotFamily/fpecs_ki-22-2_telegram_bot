from . import textAndVoice, fun
from aiogram import types, Dispatcher

def register_handlers_misc(dp: Dispatcher):
    dp.register_message_handler(textAndVoice.voice, commands=['voice'])
    dp.register_message_handler(textAndVoice.voiceAns, content_types=['voice'])
    dp.register_callback_query_handler(textAndVoice.acceptVoice, text=['acceptVoice_Ua', 'acceptVoice_Ru'])
    dp.register_message_handler(fun.sex, commands=['sex'])
    dp.register_message_handler(fun.kuni, commands=['kuni'])
    dp.register_message_handler(fun.blowjob, commands=['blowjob'])

    dp.register_message_handler(fun.getSexUser, commands=['sex_user'])
#    dp.register_message_handler(fun.info, commands=['info'])