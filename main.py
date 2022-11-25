""""
@dp.message_handler(commands=['NAME'])
async def NAME(message: types.Message):
    print(message.from_user.full_name + ' || @' + message.from_user.username + ' || ' + message.text)
    await message.answer()
"""
import requests
import asyncio
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import time, gspread
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types import InputFile
from aiogram.dispatcher.filters import Text
from aiogram.utils import executor
from datetime import datetime
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

import config

startTime = datetime.now()
bot = Bot(token=config.TOKEN, parse_mode='HTML')
dp = Dispatcher(bot)
worksheet = gspread.service_account(filename='level-slate-280111-4930953f5702.json').open_by_url('https://docs.google.com/spreadsheets/d/1ZLodGxsGLLxDdzVbpING0jcJImsyOAW1S9y8NcAs2_w/edit#gid=2127480627').get_worksheet(0)


notifyFile = open("notify.txt", "r")
notifyUsers = set ()
for line in notifyFile:
    notifyUsers.add(line.strip())
notifyFile.close()

@dp.message_handler(commands=['status'])
async def status(message: types.Message):
    print(message.from_user.full_name + ' || ' + str(message.from_user.id) + ' || ' + message.text)
    status = "I am Alive!\n"
    status += "Uptime: " + str((datetime.now() - startTime))
    await bot.send_photo(chat_id=message.from_user.id, photo=InputFile('assets/timetable/1.jpg'))


## Расписание на всю неделю
@dp.message_handler(commands=['timetable'])
async def timetable(message: types.Message):
    print(message.from_user.full_name + ' || ' + str(message.from_user.id) + ' || ' + message.text)
    first = worksheet.acell('C4:F4').value
    second = worksheet.acell('C6:F6').value
    third = worksheet.acell('C8:F8').value
    fourth = worksheet.acell('C10:F10').value
    text = "    ◀ Понеділок ▶ 🔶  \n"
    text += "════════════════\n"
    text += "Ⅰ.   [08.00 - 09.20]\n<b>" + str(first) + "</b>\n"
    text += "Ⅱ.  [09.35 - 10.55]\n<b>" + str(second) + "</b>\n"
    text += "Ⅲ. [11.10 - 12.30]\n<b>" + str(third) + "</b>\n"
    text += "Ⅳ. [12.45 - 14.05]\n<b>" + str(fourth) + "</b>\n"
    first = worksheet.acell('C3:F3').value
    second = worksheet.acell('C5:F5').value
    third = worksheet.acell('C7:F7').value
    fourth = worksheet.acell('C9:F9').value
    text += "    ◀ Понеділок ▶ 🔷  \n"
    text += "════════════════\n"
    text += "Ⅰ.   [08.00 - 09.20]\n<b>" + str(first) + "</b>\n"
    text += "Ⅱ.  [09.35 - 10.55]\n<b>" + str(second) + "</b>\n"
    text += "Ⅲ. [11.10 - 12.30]\n<b>" + str(third) + "</b>\n"
    text += "Ⅳ. [12.45 - 14.05]\n<b>" + str(fourth) + "</b>\n"
    first = worksheet.acell('C14:F14').value
    second = worksheet.acell('C16:F16').value
    third = worksheet.acell('C18:F18').value
    fourth = worksheet.acell('C20:F20').value
    text += "    ◀ Вівторок ▶ 🔶  \n"
    text += "════════════════\n"
    text += "Ⅰ.   [08.00 - 09.20]\n<b>" + str(first) + "</b>\n"
    text += "Ⅱ.  [09.35 - 10.55]\n<b>" + str(second) + "</b>\n"
    text += "Ⅲ. [11.10 - 12.30]\n<b>" + str(third) + "</b>\n"
    text += "Ⅳ. [12.45 - 14.05]\n<b>" + str(fourth) + "</b>\n"
    first = worksheet.acell('C13:F13').value
    second = worksheet.acell('C15:F15').value
    third = worksheet.acell('C17:F17').value
    fourth = worksheet.acell('C19:F19').value
    text += "    ◀ Вівторок ▶ 🔷  \n"
    text += "════════════════\n"
    text += "Ⅰ.   [08.00 - 09.20]\n<b>" + str(first) + "</b>\n"
    text += "Ⅱ.  [09.35 - 10.55]\n<b>" + str(second) + "</b>\n"
    text += "Ⅲ. [11.10 - 12.30]\n<b>" + str(third) + "</b>\n"
    text += "Ⅳ. [12.45 - 14.05]\n<b>" + str(fourth) + "</b>\n"
    first = worksheet.acell('C24:F24').value
    second = worksheet.acell('C26:F26').value
    third = worksheet.acell('C28:F28').value
    fourth = worksheet.acell('C30:F30').value
    text += "    ◀ Середа ▶ 🔶  \n"
    text += "════════════════\n"
    text += "Ⅰ.   [08.00 - 09.20]\n<b>" + str(first) + "</b>\n"
    text += "Ⅱ.  [09.35 - 10.55]\n<b>" + str(second) + "</b>\n"
    text += "Ⅲ. [11.10 - 12.30]\n<b>" + str(third) + "</b>\n"
    text += "Ⅳ. [12.45 - 14.05]\n<b>" + str(fourth) + "</b>\n"
    first = worksheet.acell('C23:F23').value
    second = worksheet.acell('C25:F25').value
    third = worksheet.acell('C27:F27').value
    fourth = worksheet.acell('C29:F29').value
    text += "    ◀ Середа ▶ 🔷  \n"
    text += "════════════════\n"
    text += "Ⅰ.   [08.00 - 09.20]\n<b>" + str(first) + "</b>\n"
    text += "Ⅱ.  [09.35 - 10.55]\n<b>" + str(second) + "</b>\n"
    text += "Ⅲ. [11.10 - 12.30]\n<b>" + str(third) + "</b>\n"
    text += "Ⅳ. [12.45 - 14.05]\n<b>" + str(fourth) + "</b>\n"
    first = worksheet.acell('C34:F34').value
    second = worksheet.acell('C36:F36').value
    third = worksheet.acell('C38:F38').value
    fourth = worksheet.acell('C40:F40').value
    text += "    ◀ Четверг ▶ 🔶  \n"
    text += "════════════════\n"
    text += "Ⅰ.   [08.00 - 09.20]\n<b>" + str(first) + "</b>\n"
    text += "Ⅱ.  [09.35 - 10.55]\n<b>" + str(second) + "</b>\n"
    text += "Ⅲ. [11.10 - 12.30]\n<b>" + str(third) + "</b>\n"
    text += "Ⅳ. [12.45 - 14.05]\n<b>" + str(fourth) + "</b>\n"
    first = worksheet.acell('C33:F33').value
    second = worksheet.acell('C35:F35').value
    third = worksheet.acell('C37:F37').value
    fourth = worksheet.acell('C39:F39').value
    text += "    ◀ Четверг ▶ 🔷  \n"
    text += "════════════════\n"
    text += "Ⅰ.   [08.00 - 09.20]\n<b>" + str(first) + "</b>\n"
    text += "Ⅱ.  [09.35 - 10.55]\n<b>" + str(second) + "</b>\n"
    text += "Ⅲ. [11.10 - 12.30]\n<b>" + str(third) + "</b>\n"
    text += "Ⅳ. [12.45 - 14.05]\n<b>" + str(fourth) + "</b>\n"
    first = worksheet.acell('C44:F44').value
    second = worksheet.acell('C46:F46').value
    third = worksheet.acell('C48:F48').value
    fourth = worksheet.acell('C50:F50').value
    text += "    ◀ П'ятниця ▶ 🔶  \n"
    text += "════════════════\n"
    text += "Ⅰ.   [08.00 - 09.20]\n<b>" + str(first) + "</b>\n"
    text += "Ⅱ.  [09.35 - 10.55]\n<b>" + str(second) + "</b>\n"
    text += "Ⅲ. [11.10 - 12.30]\n<b>" + str(third) + "</b>\n"
    text += "Ⅳ. [12.45 - 14.05]\n<b>" + str(fourth) + "</b>\n"
    first = worksheet.acell('C43:F43').value
    second = worksheet.acell('C45:F45').value
    third = worksheet.acell('C47:F47').value
    fourth = worksheet.acell('C49:F49').value
    text += "    ◀ П'ятниця ▶ 🔷 \n"
    text += "════════════════\n"
    text += "Ⅰ.   [08.00 - 09.20]\n<b>" + str(first) + "</b>\n"
    text += "Ⅱ.  [09.35 - 10.55]\n<b>" + str(second) + "</b>\n"
    text += "Ⅲ. [11.10 - 12.30]\n<b>" + str(third) + "</b>\n"
    text += "Ⅳ. [12.45 - 14.05]\n<b>" + str(fourth) + "</b>\n"
    await bot.send_message(chat_id=message.chat.id, text=text)


## Расписание на понедельник
@dp.message_handler(commands=['monday'])
async def monday(message: types.Message):
    week = datetime.date(datetime.today()).strftime("%V")
    print(message.from_user.full_name + ' || ' + str(message.from_user.id) + ' || ' + message.text)
    if int(week) % 2 == 0:
            first=worksheet.acell('C4:F4').value
            second=worksheet.acell('C6:F6').value
            third=worksheet.acell('C8:F8').value
            fourth=worksheet.acell('C10:F10').value
            text = "    ◀ Понеділок ▶ 🔶  \n"
            text += "════════════════\n"
            text += "Ⅰ.   [08.00 - 09.20]\n<b>" + str(first) + "</b>\n"
            text += "Ⅱ.  [09.35 - 10.55]\n<b>" + str(second) + "</b>\n"
            text += "Ⅲ. [11.10 - 12.30]\n<b>" + str(third) + "</b>\n"
            text += "Ⅳ. [12.45 - 14.05]\n<b>" + str(fourth) + "</b>\n"
            await bot.send_message(chat_id=message.chat.id, text=text)
    else:
            first=worksheet.acell('C3:F3').value
            second=worksheet.acell('C5:F5').value
            third=worksheet.acell('C7:F7').value
            fourth=worksheet.acell('C9:F9').value
            text = "    ◀ Понеділок ▶ 🔷  \n"
            text += "════════════════\n"
            text += "Ⅰ.   [08.00 - 09.20]\n<b>" + str(first) + "</b>\n"
            text += "Ⅱ.  [09.35 - 10.55]\n<b>" + str(second) + "</b>\n"
            text += "Ⅲ. [11.10 - 12.30]\n<b>" + str(third) + "</b>\n"
            text += "Ⅳ. [12.45 - 14.05]\n<b>" + str(fourth) + "</b>\n"
            await bot.send_message(chat_id=message.chat.id, text=text)



## Расписание на вторник
@dp.message_handler(commands=['tuesday'])
async def tuesday(message: types.Message):
    week = datetime.date(datetime.today()).strftime("%V")
    print(message.from_user.full_name + ' || ' + str(message.from_user.id) + ' || ' + message.text)
    if int(week) % 2 == 0:
            first=worksheet.acell('C14:F14').value
            second=worksheet.acell('C16:F16').value
            third=worksheet.acell('C18:F18').value
            fourth=worksheet.acell('C20:F20').value
            text = "    ◀ Вівторок ▶ 🔶  \n"
            text += "════════════════\n"
            text += "Ⅰ.   [08.00 - 09.20]\n<b>" + str(first) + "</b>\n"
            text += "Ⅱ.  [09.35 - 10.55]\n<b>" + str(second) + "</b>\n"
            text += "Ⅲ. [11.10 - 12.30]\n<b>" + str(third) + "</b>\n"
            text += "Ⅳ. [12.45 - 14.05]\n<b>" + str(fourth) + "</b>\n"
            await bot.send_message(chat_id=message.chat.id, text=text)
    else:
            first=worksheet.acell('C13:F13').value
            second=worksheet.acell('C15:F15').value
            third=worksheet.acell('C17:F17').value
            fourth=worksheet.acell('C19:F19').value
            text = "    ◀ Вівторок ▶ 🔷  \n"
            text += "════════════════\n"
            text += "Ⅰ.   [08.00 - 09.20]\n<b>" + str(first) + "</b>\n"
            text += "Ⅱ.  [09.35 - 10.55]\n<b>" + str(second) + "</b>\n"
            text += "Ⅲ. [11.10 - 12.30]\n<b>" + str(third) + "</b>\n"
            text += "Ⅳ. [12.45 - 14.05]\n<b>" + str(fourth) + "</b>\n"
            await bot.send_message(chat_id=message.chat.id, text=text)



## Расписание на среду
@dp.message_handler(commands=['wednesday'])
async def wednesday(message: types.Message):
    week = datetime.date(datetime.today()).strftime("%V")
    print(message.from_user.full_name + ' || ' + str(message.from_user.id) + ' || ' + message.text)
    if int(week) % 2 == 0:
            first=worksheet.acell('C24:F24').value
            second=worksheet.acell('C26:F26').value
            third=worksheet.acell('C28:F28').value
            fourth=worksheet.acell('C30:F30').value
            text = "    ◀ Середа ▶ 🔶  \n"
            text += "════════════════\n"
            text += "Ⅰ.   [08.00 - 09.20]\n<b>" + str(first) + "</b>\n"
            text += "Ⅱ.  [09.35 - 10.55]\n<b>" + str(second) + "</b>\n"
            text += "Ⅲ. [11.10 - 12.30]\n<b>" + str(third) + "</b>\n"
            text += "Ⅳ. [12.45 - 14.05]\n<b>" + str(fourth) + "</b>\n"
            await bot.send_message(chat_id=message.chat.id, text=text)
    else:
            first=worksheet.acell('C23:F23').value
            second=worksheet.acell('C25:F25').value
            third=worksheet.acell('C27:F27').value
            fourth=worksheet.acell('C29:F29').value
            text = "    ◀ Середа ▶ 🔷  \n"
            text += "════════════════\n"
            text += "Ⅰ.   [08.00 - 09.20]\n<b>" + str(first) + "</b>\n"
            text += "Ⅱ.  [09.35 - 10.55]\n<b>" + str(second) + "</b>\n"
            text += "Ⅲ. [11.10 - 12.30]\n<b>" + str(third) + "</b>\n"
            text += "Ⅳ. [12.45 - 14.05]\n<b>" + str(fourth) + "</b>\n"
            await bot.send_message(chat_id=message.chat.id, text=text)


## Расписание на четверг
@dp.message_handler(commands=['thursday'])
async def thursday(message: types.Message):
    week = datetime.date(datetime.today()).strftime("%V")
    print(message.from_user.full_name + ' || ' + str(message.from_user.id) + ' || ' + message.text)
    if int(week) % 2 == 0:
            first=worksheet.acell('C34:F34').value
            second=worksheet.acell('C36:F36').value
            third=worksheet.acell('C38:F38').value
            fourth=worksheet.acell('C40:F40').value
            text = "    ◀ Четверг ▶ 🔶  \n"
            text += "════════════════\n"
            text += "Ⅰ.   [08.00 - 09.20]\n<b>" + str(first) + "</b>\n"
            text += "Ⅱ.  [09.35 - 10.55]\n<b>" + str(second) + "</b>\n"
            text += "Ⅲ. [11.10 - 12.30]\n<b>" + str(third) + "</b>\n"
            text += "Ⅳ. [12.45 - 14.05]\n<b>" + str(fourth) + "</b>\n"
            await bot.send_message(chat_id=message.chat.id, text=text)
    else:
            first=worksheet.acell('C33:F33').value
            second=worksheet.acell('C35:F35').value
            third=worksheet.acell('C37:F37').value
            fourth=worksheet.acell('C39:F39').value
            text = "    ◀ Четверг ▶ 🔷  \n"
            text += "════════════════\n"
            text += "Ⅰ.   [08.00 - 09.20]\n<b>" + str(first) + "</b>\n"
            text += "Ⅱ.  [09.35 - 10.55]\n<b>" + str(second) + "</b>\n"
            text += "Ⅲ. [11.10 - 12.30]\n<b>" + str(third) + "</b>\n"
            text += "Ⅳ. [12.45 - 14.05]\n<b>" + str(fourth) + "</b>\n"
            await bot.send_message(chat_id=message.chat.id, text=text)


## Расписание на пятницу
@dp.message_handler(commands=['friday'])
async def friday(message: types.Message):
    week = datetime.date(datetime.today()).strftime("%V")
    print(message.from_user.full_name + ' || ' + str(message.from_user.id) + ' || ' + message.text)
    if int(week) % 2 == 0:
        first = worksheet.acell('C44:F44').value
        second = worksheet.acell('C46:F46').value
        third = worksheet.acell('C48:F48').value
        fourth = worksheet.acell('C50:F50').value
        text = "    ◀ П'ятниця ▶ 🔶  \n"
        text += "════════════════\n"
        text += "Ⅰ.   [08.00 - 09.20]\n<b>" + str(first) + "</b>\n"
        text += "Ⅱ.  [09.35 - 10.55]\n<b>" + str(second) + "</b>\n"
        text += "Ⅲ. [11.10 - 12.30]\n<b>" + str(third) + "</b>\n"
        text += "Ⅳ. [12.45 - 14.05]\n<b>" + str(fourth) + "</b>\n"
        await bot.send_message(chat_id=message.chat.id, text=text)
    else:
        first = worksheet.acell('C43:F43').value
        second = worksheet.acell('C45:F45').value
        third = worksheet.acell('C47:F47').value
        fourth = worksheet.acell('C49:F49').value
        text = "    ◀ П'ятниця ▶ 🔷 \n"
        text += "════════════════\n"
        text += "Ⅰ.   [08.00 - 09.20]\n<b>" + str(first) + "</b>\n"
        text += "Ⅱ.  [09.35 - 10.55]\n<b>" + str(second) + "</b>\n"
        text += "Ⅲ. [11.10 - 12.30]\n<b>" + str(third) + "</b>\n"
        text += "Ⅳ. [12.45 - 14.05]\n<b>" + str(fourth) + "</b>\n"
        await bot.send_message(chat_id=message.chat.id, text=text)




## Расписание на сегодня
@dp.message_handler(commands=['today'])
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
@dp.message_handler(commands=['tomorrow'])
async def today(message: types.Message):
    print(message.from_user.full_name + ' || ' + str(message.from_user.id) + ' || ' + message.text)
    if datetime.weekday(datetime.today()) == 6:
        await monday(message)
    if datetime.weekday(datetime.today()) == 0:
        await tuesday(message)
    if datetime.weekday(datetime.today()) == 1:
        await wednesday(message)
    if datetime.weekday(datetime.today()) == 2:
        await thursday(message)
    if datetime.weekday(datetime.today()) == 3:
        await friday(message)




async def newday():
    global newday_mess
    if datetime.weekday(datetime.today()) == 0:
        newday_mess = await monday(chat_id=-1001709052184)
    if datetime.weekday(datetime.today()) == 1:
        newday_mess = await tuesday(chat_id=-1001709052184)
    if datetime.weekday(datetime.today()) == 2:
        newday_mess = await wednesday(chat_id=-1001709052184)
    if datetime.weekday(datetime.today()) == 3:
        newday_mess = await thursday(chat_id=-1001709052184)
    if datetime.weekday(datetime.today()) == 4:
        newday_mess = await friday(chat_id=-1001709052184)
    await bot.pin_chat_message(chat_id=newday_mess.chat.id, message_id=newday_mess.message_id)

async def notify(pars):
    global newday_mess
    week = datetime.date(datetime.today()).strftime("%V")
    for user in notifyUsers:
        if int(week) % 2 == 0:
            if datetime.weekday(datetime.today()) == 0:
                if int(pars) == 3:
                    await bot.send_message(chat_id=user,
                                           text=f'Через 5 минут начнется пара {config.mon_b_3}')
                if int(pars) == 4:
                    await bot.send_message(chat_id=user,
                                           text=f'Через 5 минут начнется пара {config.mon_4}')
            if datetime.weekday(datetime.today()) == 1:
                if int(pars) == 1:
                    await bot.send_message(chat_id=user,
                                           text=f'Через 5 минут начнется пара {config.tue_b_1}')
                if int(pars) == 2:
                    await bot.send_message(chat_id=user,
                                           text=f'Через 5 минут начнется пара {config.tue_2}')
                if int(pars) == 3:
                    await bot.send_message(chat_id=user,
                                           text=f'Через 5 минут начнется пара {config.tue_3}')
            if datetime.weekday(datetime.today()) == 2:
                if int(pars) == 1:
                    await bot.send_message(chat_id=user,
                                           text=f'Через 5 минут начнется пара {config.wed_1}')
                if int(pars) == 3:
                    await bot.send_message(chat_id=user,
                                           text=f'Через 5 минут начнется пара {config.wed_b_3}')
                if int(pars) == 4:
                    await bot.send_message(chat_id=user,
                                           text=f'Через 5 минут начнется пара {config.wed_b_4}')
            if datetime.weekday(datetime.today()) == 3:
                if int(pars) == 2:
                    await bot.send_message(chat_id=user,
                                           text=f'Через 5 минут начнется пара {config.thu_b_2}')
                if int(pars) == 3:
                    await bot.send_message(chat_id=user,
                                           text=f'Через 5 минут начнется пара {config.thu_b_3}')
                if int(pars) == 4:
                    await bot.send_message(chat_id=user,
                                           text=f'Через 5 минут начнется пара {config.thu_4}')
            if datetime.weekday(datetime.today()) == 4:
                if int(pars) == 1:
                    await bot.send_message(chat_id=user,
                                           text=f'Через 5 минут начнется пара {config.fri_1}')
                if int(pars) == 2:
                    await bot.send_message(chat_id=user,
                                           text=f'Через 5 минут начнется пара {config.fri_2}')
                if int(pars) == 3:
                    await bot.send_message(chat_id=user,
                                           text=f'Через 5 минут начнется пара {config.fri_3}')
                if int(pars) == 4:
                    pass
        else:
            if datetime.weekday(datetime.today()) == 0:
                if int(pars) == 3:
                    await bot.send_message(chat_id=user,
                                           text=f'Через 5 минут начнется пара {config.mon_a_3}')
                if int(pars) == 4:
                    await bot.send_message(chat_id=user,
                                           text=f'Через 5 минут начнется пара {config.mon_4}')
            if datetime.weekday(datetime.today()) == 1:
                if int(pars) == 1:
                    await bot.send_message(chat_id=user,
                                           text=f'Через 5 минут начнется пара {config.tue_a_1}')
                if int(pars) == 2:
                    await bot.send_message(chat_id=user,
                                           text=f'Через 5 минут начнется пара {config.tue_2}')
                if int(pars) == 3:
                    await bot.send_message(chat_id=user,
                                           text=f'Через 5 минут начнется пара {config.tue_3}')
            if datetime.weekday(datetime.today()) == 2:
                if int(pars) == 1:
                    await bot.send_message(chat_id=user,
                                           text=f'Через 5 минут начнется пара {config.wed_1}')
                if int(pars) == 2:
                    await bot.send_message(chat_id=user,
                                           text=f'Через 5 минут начнется пара {config.wed_a_2}')
                if int(pars) == 3:
                    await bot.send_message(chat_id=user,
                                           text=f'Через 5 минут начнется пара {config.wed_a_3}')
                if int(pars) == 4:
                    await bot.send_message(chat_id=user,
                                           text=f'Через 5 минут начнется пара {config.wed_a_4}')
                pass
            if datetime.weekday(datetime.today()) == 3:
                if int(pars) == 2:
                    await bot.send_message(chat_id=user,
                                           text=f'Через 5 минут начнется пара {config.thu_a_2}')
                if int(pars) == 3:
                    await bot.send_message(chat_id=user,
                                           text=f'Через 5 минут начнется пара {config.thu_a_3}')
                if int(pars) == 4:
                    await bot.send_message(chat_id=user,
                                           text=f'Через 5 минут начнется пара {config.thu_4}')
            if datetime.weekday(datetime.today()) == 4:
                if int(pars) == 1:
                    await bot.send_message(chat_id=user,
                                           text=f'Через 5 минут начнется пара {config.fri_1}')
                if int(pars) == 2:
                    await bot.send_message(chat_id=user,
                                           text=f'Через 5 минут начнется пара {config.fri_2}')
                if int(pars) == 3:
                    await bot.send_message(chat_id=user,
                                           text=f'Через 5 минут начнется пара {config.fri_3}')


@dp.message_handler(commands=['notify_on'])
async def notify_on(message: types.Message):
    notifyFile = open("notify.txt", "r")
    if not str(message.chat.id) in notifyFile:
        notifyFile.close()
        notifyFile = open("notify.txt", "a")
        notifyFile.write(str(message.chat.id) + "\n")
        notifyUsers.add(message.chat.id)
        await bot.send_message(message.chat.id, 'Уведомления включены')

scheduler = AsyncIOScheduler()
scheduler.add_job(newday, 'cron', day_of_week='mon-fri', hour='5', minute='00')
scheduler.add_job(notify, 'cron', day_of_week='mon-fri', hour='04', minute='55', args=('1'))
scheduler.add_job(notify, 'cron', day_of_week='mon-fri', hour='06', minute='30', args=('2'))
scheduler.add_job(notify, 'cron', day_of_week='mon-fri', hour='08', minute='05', args=('3'))
scheduler.add_job(notify, 'cron', day_of_week='mon-fri', hour='09', minute='40', args=('4'))
scheduler.start()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)
