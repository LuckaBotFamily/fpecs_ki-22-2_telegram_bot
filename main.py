""""
@dp.message_handler(commands=['NAME'])
async def NAME(message: types.Message):
    print(message.from_user.full_name + ' || @' + message.from_user.username + ' || ' + message.text)
    await message.answer()
"""
import schedule
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types import InputFile
from aiogram.utils import executor
from datetime import datetime

import config
startTime = datetime.now()
bot = Bot(token=config.TOKEN, parse_mode='HTML')
dp = Dispatcher(bot)


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
async def wednesday(message: types.Message):
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

if __name__ == '__main__':
    executor.start_polling(dp)