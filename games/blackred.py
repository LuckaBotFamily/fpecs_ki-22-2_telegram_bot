import random
import time
from create_bot import bot
from aiogram import types

async def blackred(message: types.Message):
    up = "===⬇=======================\n"
    down = "\n===⬆======================="
    char = "◼◼◼◼◼◼◼◼◼◼"
    mess = await bot.send_message(chat_id=message.chat.id, text=up + char + down)
    num = random.randint(1, 2)
    if num == 1:
        char = "🔴"
    if num == 2:
        char = "⚫"
    i = 0
    while(i < 10):
        if char[i] == "⚫":
            char += "🔴"
        else:
            char += "⚫"
        if i == 4 or i == 8 or i == 12 or i == 16 or i > 18:
            await bot.edit_message_text(chat_id=message.chat.id, message_id=mess.message_id, text=up + char[0:10] + down)
        i = i + 1