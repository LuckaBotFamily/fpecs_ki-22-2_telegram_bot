from aiogram import types, Dispatcher
from create_bot import dp, bot
from datetime import datetime
import gspread
from keyboards.inline import inline_delete
from . import days_mess

worksheet = gspread.service_account(filename='level-slate-280111-4930953f5702.json').open_by_url('https://docs.google.com/spreadsheets/d/1ZLodGxsGLLxDdzVbpING0jcJImsyOAW1S9y8NcAs2_w/edit#gid=2127480627').get_worksheet(0)

async def forward_mess(message, text):
    await bot.send_message(chat_id=message.chat.id, text=text, reply_markup=inline_delete)
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)

async def monday(message: types.Message):
    text = days_mess.day_mess("monday", datetime.date(datetime.today()).strftime("%V"))
    await forward_mess(message, text)

async def tuesday(message: types.Message):
    text = days_mess.day_mess("tuesday", datetime.date(datetime.today()).strftime("%V"))
    await forward_mess(message, text)


async def wednesday(message: types.Message):
    text = days_mess.day_mess("wednesday", datetime.date(datetime.today()).strftime("%V"))
    await forward_mess(message, text)


async def thursday(message: types.Message):
    text = days_mess.day_mess("thursday", datetime.date(datetime.today()).strftime("%V"))
    await forward_mess(message, text)


async def friday(message: types.Message):
    text = days_mess.day_mess("friday", datetime.date(datetime.today()).strftime("%V"))
    await forward_mess(message, text)



async def today(message: types.Message):
    print(message.from_user.full_name + ' || ' + str(message.from_user.id) + ' || ' + message.text)
    if datetime.weekday(datetime.today()) == 0:
        await monday(message)
    if datetime.weekday(datetime.today()) == 1:
        await tuesday(message)
    if datetime.weekday(datetime.today()) == 2:
        await wednesday(message)
    if datetime.weekday(datetime.today()) == 3:
        await thursday(message)
    if datetime.weekday(datetime.today()) == 4:
        await friday(message)

## Расписание на завтра
async def tomorrow(message: types.Message):
    print(message.from_user.full_name + ' || ' + str(message.from_user.id) + ' || ' + message.text)
    if datetime.weekday(datetime.today()) > 3:
        text = days_mess.day_mess("monday", week=int(datetime.date(datetime.today()).strftime("%V"))+1)
        await forward_mess(message, text)
    if datetime.weekday(datetime.today()) == 0:
        await tuesday(message)
    if datetime.weekday(datetime.today()) == 1:
        await wednesday(message)
    if datetime.weekday(datetime.today()) == 2:
        await thursday(message)
    if datetime.weekday(datetime.today()) == 3:
        await friday(message)

def register_handlers_days(dp: Dispatcher):
    dp.register_message_handler(monday, commands=['monday'])
    dp.register_message_handler(tuesday, commands=['tuesday'])
    dp.register_message_handler(wednesday, commands=['wednesday'])
    dp.register_message_handler(thursday, commands=['thursday'])
    dp.register_message_handler(friday, commands=['friday'])
    dp.register_message_handler(today, commands=['today'])
    dp.register_message_handler(tomorrow, commands=['tomorrow'])