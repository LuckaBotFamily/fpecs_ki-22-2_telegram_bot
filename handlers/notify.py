from datetime import datetime
from aiogram import types, Dispatcher
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from .days import monday, tuesday, wednesday, thursday, friday
from create_bot import bot, dp

notifyFile = open("notify.txt", "r")
notifyUsers = set ()
for line in notifyFile:
    notifyUsers.add(line.strip())
notifyFile.close()

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

async def notify_on(message: types.Message):
    notifyFile = open("notify.txt", "r")
    if not str(message.chat.id) in notifyFile:
        notifyFile.close()
        notifyFile = open("notify.txt", "a")
        notifyFile.write(str(message.chat.id) + "\n")
        notifyUsers.add(message.chat.id)
        await bot.send_message(message.chat.id, 'Уведомления включены')


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


scheduler = AsyncIOScheduler()
scheduler.add_job(newday, 'cron', day_of_week='mon-fri', hour='5', minute='00')
scheduler.add_job(notify, 'cron', day_of_week='mon-fri', hour='04', minute='55', args=('1'))
scheduler.add_job(notify, 'cron', day_of_week='mon-fri', hour='06', minute='30', args=('2'))
scheduler.add_job(notify, 'cron', day_of_week='mon-fri', hour='08', minute='05', args=('3'))
scheduler.add_job(notify, 'cron', day_of_week='mon-fri', hour='09', minute='40', args=('4'))
scheduler.start()

def register_handlers_notify(dp: Dispatcher):
    dp.register_message_handler(notify_on, commands=['notify_on'])