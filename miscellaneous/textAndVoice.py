from create_bot import bot, dp
import logger
from aiogram import types, Dispatcher
from aiogram.types import InputFile
from keyboards.inline import inline_delete

import gtts

async def voice(message: types.Message):
    try:
        text = message.reply_to_message.text
    except:
        text = message.text[6:]
    tts = gtts.gTTS(f'{text}', lang='ru')
    tts.save('voice.mp3')
    await bot.send_voice(chat_id=message.chat.id, voice=InputFile('voice.mp3'))
    await logger.logger_mess(message)
