from aiogram import types, Dispatcher
import gspread
from create_bot import dp, bot
from datetime import datetime
from keyboards.inline import inline_delete

worksheet = gspread.service_account(filename='level-slate-280111-4930953f5702.json').open_by_url('https://docs.google.com/spreadsheets/d/1ZLodGxsGLLxDdzVbpING0jcJImsyOAW1S9y8NcAs2_w/edit#gid=2127480627').get_worksheet(0)


## Расписание на понедельник
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
    await bot.send_message(chat_id=message.chat.id, text=text, reply_markup=inline_delete)
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)



## Расписание на вторник
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
    await bot.send_message(chat_id=message.chat.id, text=text, reply_markup=inline_delete)
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)



## Расписание на среду
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
    await bot.send_message(chat_id=message.chat.id, text=text, reply_markup=inline_delete)
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)


## Расписание на четверг
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
    await bot.send_message(chat_id=message.chat.id, text=text, reply_markup=inline_delete)
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)


## Расписание на пятницу
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
    await bot.send_message(chat_id=message.chat.id, text=text, reply_markup=inline_delete)
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)




## Расписание на сегодня
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

def register_handlers_days(dp: Dispatcher):
    dp.register_message_handler(monday, commands=['monday'])
    dp.register_message_handler(tuesday, commands=['tuesday'])
    dp.register_message_handler(wednesday, commands=['wednesday'])
    dp.register_message_handler(thursday, commands=['thursday'])
    dp.register_message_handler(friday, commands=['friday'])
    dp.register_message_handler(today, commands=['today'])
    dp.register_message_handler(tomorrow, commands=['tomorrow'])
