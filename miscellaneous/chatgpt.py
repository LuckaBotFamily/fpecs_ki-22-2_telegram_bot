import time

import openai
from aiogram import types, Dispatcher
import config
from create_bot import bot, dp


openai.api_key = config.OPENAI
messages = {}



@dp.message_handler(commands=['newtopic'])
async def new_topic_cmd(message: types.Message):
        username = message.from_user.username
        messages[username] = []
        await message.reply('Starting a new topic! * * * \n\nНачинаем новую тему! * * *', parse_mode='Markdown')

async def chatGptMess(message: types.Message):
    if "ОТКИСОН" in message.text.split()[0].upper():
        user_message = message.text
        username = message.from_user.username

        if username not in messages:
            messages[username] = []
        messages[username].append({"role": "user", "content": user_message})
        messages[username].append({"role": "user", "content": f"chat: {message.chat} Сейчас время {time.strftime('%d/%m/%Y %H:%M:%S')} user: {message.from_user.first_name} message: {message.text}"})

        should_respond = not message.reply_to_message or message.reply_to_message.from_user.id == bot.id

        if should_respond:
            completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages[username],
                max_tokens=1500,
                temperature=0.7,
                frequency_penalty=0,
                presence_penalty=0,
                user=username
            )
            chatgpt_response = completion.choices[0]['message']
            messages[username].append({"role": "assistant", "content": chatgpt_response['content']})
            await message.reply(chatgpt_response['content'], parse_mode='Markdown')
