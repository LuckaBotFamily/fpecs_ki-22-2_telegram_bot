log_chat = -1001747950253
bot_name = "FPECS | KI-22-2"

from create_bot import bot, dp
from aiogram import types, Dispatcher

async def logger_mess(message: types.Message):
    text = f"Bot >> {bot_name}\n"
    text += f'User >> <a href="tg://user?id={message.from_user.id}">{message.from_user.full_name}</a>\n'
    text += f"Type >> message_handler\n"
    if message.from_user.id == message.chat.id:
        chat_type = "PM"
    else:
        chat_type = "Chat"
    text += f"Chat type >> {chat_type}\n"
    if chat_type == "Chat":
        text += f"  ChatId >> {message.chat.id}\n"
    text += f"Command >> {message.text}"
    await bot.send_message(chat_id=log_chat, text=text)

async def logger_cq(command, call: types.CallbackQuery):
    text = f"Bot >> {bot_name}\n"
    text += f'User >> <a href="tg://user?id={call.from_user.id}">{call.from_user.full_name}</a>\n'
    text += f"Type >> callback_query\n"
    if call.from_user.id == call.message.chat.id:
        chat_type = "PM"
    else:
        chat_type = "Chat"
    text += f"Chat type >> {chat_type}\n"
    if chat_type == "Chat":
        text += f"  ChatId >> {call.message.chat.id}\n"
    text += f"Command >> {command}"
    await bot.send_message(chat_id=log_chat, text=text)

async def logger_notify(users):
    text = f"Bot >> {bot_name}\n"
    text += f"Type >> notify_handler\n"
    text += f"Users: {users}"
    await bot.send_message(chat_id=log_chat, text=text)

async def logger_newday():
    text = f"Bot >> {bot_name}\n"
    text += f"Type >> notify_newday\n"
    await bot.send_message(chat_id=log_chat, text=text)