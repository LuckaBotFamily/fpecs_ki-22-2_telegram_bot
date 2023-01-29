import random

from create_bot import bot, dp
import logger, config
from aiogram import types, Dispatcher
# 29.01.23 TODO: Переделать на нормальную базу, а то щас ряльно кринж
usrsSex = ['586715737', '456391767', '1211580868', '576092040', '714713631', '786290626', '750915341', '999694590', '467991052', '1414646966', '602838745']
async def sex(message: types.Message):
    try:
        text = f"Ви успішно зайнялися сексом з <a href='tg://user?id={message.reply_to_message.from_user.id}'>{message.reply_to_message.from_user.full_name}</a>"
    except:
        usr = await bot.get_chat_member(chat_id=message.chat.id, user_id=usrsSex[random.randint(0, 10)])
        text = f"Ви успішно зайнялися сексом з <a href='tg://user?id={usr.user.id}'>{usr.user.full_name}</a>"
    await bot.send_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, text=text)
    await logger.logger_mess(message)

async def getSexUser(message: types.Message):
    text = "Претенденти на випадковий секс:"
    for user in usrsSex:
            usr = await bot.get_chat_member(chat_id=message.chat.id, user_id=user)
            text += f"\n<a href='tg://user?id={usr.user.id}'>{usr.user.full_name}</a>"
    await bot.send_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, text=text)
    await logger.logger_mess(message)

#async def info(message: types.Message):
#    usr = await bot.get_chat_member(chat_id=message.chat.id, user_id=message.reply_to_message.from_user.id)
#    print(usr)
#    await bot.send_message(chat_id=message.chat.id, text=f"{usr.user.first_name} \nid- {usr.user.id}")