from create_bot import bot, dp
import logger, config
from aiogram import types, Dispatcher
from aiogram.types import InputFile
from keyboards.inline import inline_acceptVoice, inline_delete

import gtts
import speech_recognition as sr
import soundfile as sf
import requests

async def voice(message: types.Message):
    try:
        text = message.reply_to_message.text
    except:
        text = message.text[6:]
    tts = gtts.gTTS(f'{text}', lang='ru')
    tts.save('voice.mp3')
    await bot.send_voice(chat_id=message.chat.id, voice=InputFile('voice.mp3'))
    await logger.logger_mess(message)


async def voiceAns(message: types.Message):
    await bot.send_message(text="Бажаєте розшифрувати голосове повідомлення?", chat_id=message.chat.id,
                           reply_to_message_id=message.message_id, reply_markup=inline_acceptVoice)

async def acceptVoice(callback_query: types.CallbackQuery):
    await bot.edit_message_text(text="Обробка, зачекайте кілька секунд....", chat_id=callback_query.message.chat.id,
                                message_id=callback_query.message.message_id, reply_markup=None)
    file_info = await bot.get_file(callback_query.message.reply_to_message.voice.file_id)
    file = requests.get('https://api.telegram.org/file/bot{0}/{1}'.format(config.TOKEN, file_info.file_path))
    if callback_query.data == 'acceptVoice_Ua':
        lang = 'uk-UA'
    elif callback_query.data == 'acceptVoice_Ru':
        lang = 'ru-RU'
    with open('voice.mp3', 'wb') as f:
        f.write(file.content)
    data, samplerate = sf.read('voice.mp3')
    sf.write('voice.wav', data, samplerate)
    r = sr.Recognizer()
    with sr.AudioFile('voice.wav') as source:
        audio_data = r.record(source)
        try:
            await bot.edit_message_text(text=r.recognize_google(audio_data, language=lang), chat_id=callback_query.message.chat.id,
                                    message_id=callback_query.message.message_id, reply_markup=inline_delete)
        except:
            await bot.edit_message_text(text="Помилка при розпізнаванні голосу", chat_id=callback_query.message.chat.id,
                                        message_id=callback_query.message.message_id, reply_markup=inline_delete)
