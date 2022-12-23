from aiogram import types, Dispatcher
import gspread
from . import days_mess
from create_bot import dp, bot
from keyboards.inline import inline_delete, list
worksheet = gspread.service_account(filename='level-slate-280111-4930953f5702.json').open_by_url('https://docs.google.com/spreadsheets/d/1ZLodGxsGLLxDdzVbpING0jcJImsyOAW1S9y8NcAs2_w/edit#gid=2127480627').get_worksheet(0)


## Расписание на всю неделю
async def timetable(message: types.Message):
    print(message.from_user.full_name + ' || ' + str(message.from_user.id) + ' || ' + message.text)
    if "full" in message.get_args():
        y = 1
        text = ""
        while (y < 6):
            text += days_mess.getFullDay(y)
            y = y + 1
        await bot.send_message(chat_id=message.chat.id, text="Відправив розклад у особисті повідомлення, щоб не засмічувати чат.", reply_markup=inline_delete)
        await bot.send_message(chat_id=message.from_user.id, text=text, reply_markup=inline_delete)
    else:
        await bot.send_message(chat_id=message.chat.id, text=days_mess.getFullDay(1), reply_markup=list)
@dp.callback_query_handler(text_startswith="left")
async def prev_page(call: types.CallbackQuery):
    if "◀ Понеділок ▶" in call.message.text:
        x = 5
    if "◀ Вівторок ▶" in call.message.text:
        x = 1
    if "◀ Середа ▶" in call.message.text:
        x = 2
    if "◀ Четверг ▶" in call.message.text:
        x = 3
    if "◀ П'ятниця ▶" in call.message.text:
        x = 4
    await call.message.edit_text(text=days_mess.getFullDay(x), reply_markup=list)


@dp.callback_query_handler(text_startswith="right")
async def next_page(call: types.CallbackQuery):
    if "◀ Понеділок ▶" in call.message.text:
        x = 2
    if "◀ Вівторок ▶" in call.message.text:
        x = 3
    if "◀ Середа ▶" in call.message.text:
        x = 4
    if "◀ Четверг ▶" in call.message.text:
        x = 5
    if "◀ П'ятниця ▶" in call.message.text:
        x = 1
    await call.message.edit_text(text=days_mess.getFullDay(x), reply_markup=list)


@dp.message_handler(commands=["test"])
async def handler(msg: types.Message):
    await msg.answer('text', reply_markup=list)

def register_handlers_days(dp: Dispatcher):
    dp.register_message_handler(timetable, commands=['timetable'])