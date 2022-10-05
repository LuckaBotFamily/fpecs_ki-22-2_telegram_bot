""""
@dp.message_handler(commands=['NAME'])
async def NAME(message: types.Message):
    print(message.from_user.full_name + ' || @' + message.from_user.username + ' || ' + message.text)
    await message.answer()
"""
import requests
import asyncio
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import time
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types import InputFile
from aiogram.utils import executor
from datetime import datetime

from bs4 import BeautifulSoup

import config

startTime = datetime.now()
bot = Bot(token=config.TOKEN, parse_mode='HTML')
dp = Dispatcher(bot)

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
    await bot.send_photo(chat_id=message.chat.id, photo=InputFile('assets/timetable/timetable.png'))


## Расписание на понедельник
@dp.message_handler(commands=['monday'])
async def monday(message: types.Message):
    week = datetime.date(datetime.today()).strftime("%V")
    print(message.from_user.full_name + ' || ' + str(message.from_user.id) + ' || ' + message.text)
    if int(week) % 2 == 0:
        await bot.send_photo(chat_id=message.chat.id, photo=InputFile('assets/timetable/mon_b.png'))
    else:
        await bot.send_photo(chat_id=message.chat.id, photo=InputFile('assets/timetable/mon_a.png'))


## Расписание на вторник
@dp.message_handler(commands=['tuesday'])
async def tuesday(message: types.Message):
    week = datetime.date(datetime.today()).strftime("%V")
    print(message.from_user.full_name + ' || ' + str(message.from_user.id) + ' || ' + message.text)
    if int(week) % 2 == 0:
        await bot.send_photo(chat_id=message.chat.id, photo=InputFile('assets/timetable/tue_b.png.png'))
    else:
        await bot.send_photo(chat_id=message.chat.id, photo=InputFile('assets/timetable/tue_a.png'))


## Расписание на среду
@dp.message_handler(commands=['wednesday'])
async def wednesday(chat_id, message: types.Message):
    week = datetime.date(datetime.today()).strftime("%V")
    print(message.from_user.full_name + ' || ' + str(message.from_user.id) + ' || ' + message.text)
    if int(week) % 2 == 0:
        await bot.send_photo(chat_id=message.chat.id, photo=InputFile('assets/timetable/wed_b.png'))
    else:
        await bot.send_photo(chat_id=message.chat.id, photo=InputFile('assets/timetable/wed_a.png'))


## Расписание на четверг
@dp.message_handler(commands=['thursday'])
async def thursday(message: types.Message):
    week = datetime.date(datetime.today()).strftime("%V")
    print(message.from_user.full_name + ' || ' + str(message.from_user.id) + ' || ' + message.text)
    if int(week) % 2 == 0:
        await bot.send_photo(chat_id=message.chat.id, photo=InputFile('assets/timetable/thu_b.png'))
    else:
        await bot.send_photo(chat_id=message.chat.id, photo=InputFile('assets/timetable/thu_a.png'))


## Расписание на пятницу
@dp.message_handler(commands=['friday'])
async def friday(message: types.Message):
    print(message.from_user.full_name + ' || ' + str(message.from_user.id) + ' || ' + message.text)
    await bot.send_photo(chat_id=message.chat.id, photo=InputFile('assets/timetable/fri.png'))


## Расписание на сегодня
@dp.message_handler(commands=['today'])
async def today(message: types.Message):
    week = datetime.date(datetime.today()).strftime("%V")
    print(message.from_user.full_name + ' || ' + str(message.from_user.id) + ' || ' + message.text)
    if int(week) % 2 == 0:
        if datetime.weekday(datetime.today()) == 0:
            await bot.send_photo(chat_id=message.chat.id, photo=InputFile('assets/timetable/mon_b.png'))
            pass
        if datetime.weekday(datetime.today()) == 1:
            await bot.send_photo(chat_id=message.chat.id, photo=InputFile('assets/timetable/tue_b.png'))
            pass
        if datetime.weekday(datetime.today()) == 2:
            await bot.send_photo(chat_id=message.chat.id, photo=InputFile('assets/timetable/wed_b.png'))
            pass
        if datetime.weekday(datetime.today()) == 3:
            await bot.send_photo(chat_id=message.chat.id, photo=InputFile('assets/timetable/thu_b.png'))
            pass
        if datetime.weekday(datetime.today()) == 4:
            await bot.send_photo(chat_id=message.chat.id, photo=InputFile('assets/timetable/fri.png'))
            pass
        if datetime.weekday(datetime.today()) == 5:
            await bot.send_photo(chat_id=message.chat.id, photo=InputFile('assets/timetable/'))
            pass
        if datetime.weekday(datetime.today()) == 6:
            await bot.send_photo(chat_id=message.chat.id, photo=InputFile('assets/timetable/'))
            pass
    else:
        if datetime.weekday(datetime.today()) == 0:
            await bot.send_photo(chat_id=message.chat.id, photo=InputFile('assets/timetable/mon_a.png'))
            pass
        if datetime.weekday(datetime.today()) == 1:
            await bot.send_photo(chat_id=message.chat.id, photo=InputFile('assets/timetable/tue_a.png'))
            pass
        if datetime.weekday(datetime.today()) == 2:
            await bot.send_photo(chat_id=message.chat.id, photo=InputFile('assets/timetable/wed_a.png'))
            pass
        if datetime.weekday(datetime.today()) == 3:
            await bot.send_photo(chat_id=message.chat.id, photo=InputFile('assets/timetable/thu_a.png'))
            pass
        if datetime.weekday(datetime.today()) == 4:
            await bot.send_photo(chat_id=message.chat.id, photo=InputFile('assets/timetable/fri.png'))
            pass
        if datetime.weekday(datetime.today()) == 5:
            await bot.send_photo(chat_id=message.chat.id, photo=InputFile('assets/timetable/'))
            pass
        if datetime.weekday(datetime.today()) == 6:
            await bot.send_photo(chat_id=message.chat.id, photo=InputFile('assets/timetable/'))
            pass


## Расписание на завтра
@dp.message_handler(commands=['tomorrow'])
async def today(message: types.Message):
    week = datetime.date(datetime.today()).strftime("%V")
    print(message.from_user.full_name + ' || ' + str(message.from_user.id) + ' || ' + message.text)
    if int(week) % 2 == 0:
        if datetime.weekday(datetime.today()) == 6:
            await bot.send_photo(chat_id=message.chat.id, photo=InputFile('assets/timetable/mon_b.png'))
            pass
        if datetime.weekday(datetime.today()) == 0:
            await bot.send_photo(chat_id=message.chat.id, photo=InputFile('assets/timetable/tue_b.png'))
            pass
        if datetime.weekday(datetime.today()) == 1:
            await bot.send_photo(chat_id=message.chat.id, photo=InputFile('assets/timetable/wed_b.png'))
            pass
        if datetime.weekday(datetime.today()) == 2:
            await bot.send_photo(chat_id=message.chat.id, photo=InputFile('assets/timetable/thu_b.png'))
            pass
        if datetime.weekday(datetime.today()) == 3:
            await bot.send_photo(chat_id=message.chat.id, photo=InputFile('assets/timetable/fri.png'))
            pass
        if datetime.weekday(datetime.today()) == 4:
            await bot.send_photo(chat_id=message.chat.id, photo=InputFile('assets/timetable/'))
            pass
        if datetime.weekday(datetime.today()) == 5:
            await bot.send_photo(chat_id=message.chat.id, photo=InputFile('assets/timetable/'))
            pass
    else:
        if datetime.weekday(datetime.today()) == 6:
            await bot.send_photo(chat_id=message.chat.id, photo=InputFile('assets/timetable/mon_a.png'))
            pass
        if datetime.weekday(datetime.today()) == 0:
            await bot.send_photo(chat_id=message.chat.id, photo=InputFile('assets/timetable/tue_a.png'))
            pass
        if datetime.weekday(datetime.today()) == 1:
            await bot.send_photo(chat_id=message.chat.id, photo=InputFile('assets/timetable/wed_a.png'))
            pass
        if datetime.weekday(datetime.today()) == 2:
            await bot.send_photo(chat_id=message.chat.id, photo=InputFile('assets/timetable/thu_a.png'))
            pass
        if datetime.weekday(datetime.today()) == 3:
            await bot.send_photo(chat_id=message.chat.id, photo=InputFile('assets/timetable/fri.png'))
            pass
        if datetime.weekday(datetime.today()) == 4:
            await bot.send_photo(chat_id=message.chat.id, photo=InputFile('assets/timetable/'))
            pass
        if datetime.weekday(datetime.today()) == 5:
            await bot.send_photo(chat_id=message.chat.id, photo=InputFile('assets/timetable/'))
            pass


async def newday():
    global newday_mess
    week = datetime.date(datetime.today()).strftime("%V")
    if int(week) % 2 == 0:
        if datetime.weekday(datetime.today()) == 0:
            newday_mess = await bot.send_photo(chat_id=-1001709052184, photo=InputFile('assets/timetable/mon_b.png'))
            pass
        if datetime.weekday(datetime.today()) == 1:
            newday_mess = await bot.send_photo(chat_id=-1001709052184, photo=InputFile('assets/timetable/tue_b.png'))
            pass
        if datetime.weekday(datetime.today()) == 2:
            newday_mess = await bot.send_photo(chat_id=-1001709052184, photo=InputFile('assets/timetable/wed_b.png'))
            pass
        if datetime.weekday(datetime.today()) == 3:
            newday_mess = await bot.send_photo(chat_id=-1001709052184, photo=InputFile('assets/timetable/thu_b.png'))
            pass
        if datetime.weekday(datetime.today()) == 4:
            newday_mess = await bot.send_photo(chat_id=-1001709052184, photo=InputFile('assets/timetable/fri.png'))
            pass
        if datetime.weekday(datetime.today()) == 5:
            newday_mess = await bot.send_photo(chat_id=-1001709052184, photo=InputFile('assets/timetable/'))
            pass
        if datetime.weekday(datetime.today()) == 6:
            newday_mess = await bot.send_photo(chat_id=-1001709052184, photo=InputFile('assets/timetable/'))
            pass
        await bot.pin_chat_message(chat_id=newday_mess.chat.id, message_id=newday_mess.message_id)
    else:
        if datetime.weekday(datetime.today()) == 0:
            newday_mess = await bot.send_photo(chat_id=-1001709052184, photo=InputFile('assets/timetable/mon_a.png'))
            pass
        if datetime.weekday(datetime.today()) == 1:
            newday_mess = await bot.send_photo(chat_id=-1001709052184, photo=InputFile('assets/timetable/tue_a.png'))
            pass
        if datetime.weekday(datetime.today()) == 2:
            newday_mess = await bot.send_photo(chat_id=-1001709052184, photo=InputFile('assets/timetable/wed_a.png'))
            pass
        if datetime.weekday(datetime.today()) == 3:
            newday_mess = await bot.send_photo(chat_id=-1001709052184, photo=InputFile('assets/timetable/thu_a.png'))
            pass
        if datetime.weekday(datetime.today()) == 4:
            newday_mess = await bot.send_photo(chat_id=-1001709052184, photo=InputFile('assets/timetable/fri.png'))
            pass
        if datetime.weekday(datetime.today()) == 5:
            newday_mess = await bot.send_photo(chat_id=-1001709052184, photo=InputFile('assets/timetable/'))
            pass
        if datetime.weekday(datetime.today()) == 6:
            newday_mess = await bot.send_photo(chat_id=-1001709052184, photo=InputFile('assets/timetable/'))
            pass
        await bot.pin_chat_message(chat_id=newday_mess.chat.id, message_id=newday_mess.message_id)


async def notify(pars):
    global newday_mess
    week = datetime.date(datetime.today()).strftime("%V")
    for user in notifyUsers:
        if int(week) % 2 == 0:
            if datetime.weekday(datetime.today()) == 0:
                if int(pars) == 2:
                    await bot.send_message(chat_id=user,
                                           text=f'Через 5 минут начнется пара {config.mon_b_2}')
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
scheduler.add_job(newday, 'cron', day_of_week='mon-fri', hour='4', minute='00')
scheduler.add_job(notify, 'cron', day_of_week='mon-fri', hour='04', minute='55', args=('1'))
scheduler.add_job(notify, 'cron', day_of_week='mon-fri', hour='06', minute='30', args=('2'))
scheduler.add_job(notify, 'cron', day_of_week='mon-fri', hour='08', minute='05', args=('3'))
scheduler.add_job(notify, 'cron', day_of_week='mon-fri', hour='09', minute='40', args=('4'))
scheduler.start()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)
