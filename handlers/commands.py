from create_bot import bot, dp
from datetime import datetime
from aiogram import types, Dispatcher


async def delete(callback_query: types.CallbackQuery):
    await callback_query.message.delete()

async def status(message: types.Message):
    print(message.from_user.full_name + ' || ' + str(message.from_user.id) + ' || ' + message.text)
    status = "I am Alive!\n"
    status += "Uptime: " + str((datetime.now() - startTime))
    await bot.send_photo(chat_id=message.from_user.id, photo=InputFile('assets/timetable/1.jpg'))

def register_handlers_commands(dp: Dispatcher):
    dp.register_message_handler(status, commands=['status'])
    dp.register_callback_query_handler(delete, text="delete")