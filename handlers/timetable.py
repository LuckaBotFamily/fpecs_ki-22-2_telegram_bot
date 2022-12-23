from aiogram import types, Dispatcher
import gspread
from . import days_mess
from create_bot import dp, bot
from keyboards.inline import inline_delete, list
worksheet = gspread.service_account(filename='level-slate-280111-4930953f5702.json').open_by_url('https://docs.google.com/spreadsheets/d/1ZLodGxsGLLxDdzVbpING0jcJImsyOAW1S9y8NcAs2_w/edit#gid=2127480627').get_worksheet(0)


## Расписание на всю неделю
async def timetable(message: types.Message):
    print(message.from_user.full_name + ' || ' + str(message.from_user.id) + ' || ' + message.text)
    y = 1
    text = ""
    while (y < 6):
        z = 1
        if y == 1:
            text += "\n\n    ◀ Понеділок ▶   \n"
        if y == 2:
            text += "\n\n    ◀ Вівторок ▶   \n"
        if y == 3:
            text += "\n\n    ◀ Середа ▶   \n"
        if y == 4:
            text += "\n\n     ◀ Четверг ▶   \n"
        if y == 5:
            text += "\n\n    ◀ П'ятниця ▶   \n"
        text += "════════════════\n"
        while (z < 5):
            up = str(days_mess.getLine(day=y, color=0, line=z))
            down = str(days_mess.getLine(day=y, color=1, line=z))
            if up != "None" and down != "None":
                if z == 1:
                    text += "Ⅰ.   [08.00 - 09.20]\n"
                if z == 2:
                    text += "Ⅱ.  [09.35 - 10.55]\n"
                if z == 3:
                    text += "Ⅲ. [11.10 - 12.30]\n"
                if z == 4:
                    text += "Ⅳ. [12.45 - 14.05]\n"
                if up == down:
                    text += up + "\n"
                else:
                    if not ("None" in up):
                        text += up + "\n"
                    if not ("None" in down):
                        text += down + "\n"
            z = z + 1
        y = y + 1
    await bot.send_message(chat_id=message.chat.id, text="Відправив розклад у особисті повідомлення, щоб не засмічувати чат.", reply_markup=inline_delete)
    await bot.send_message(chat_id=message.from_user.id, text=text, reply_markup=inline_delete)

@dp.callback_query_handler(text_startswith="prev")
async def prev_page(call: types.CallbackQuery):
    await call.answer()
    await call.message.edit_text("text", reply_markup=list)


@dp.callback_query_handler(text_startswith="next")
async def next_page(call: types.CallbackQuery):
    await call.answer()
    await call.message.edit_text("text", reply_markup=list)


@dp.message_handler(commands=["test"])
async def handler(msg: types.Message):
    await msg.answer('text', reply_markup=list)

def register_handlers_days(dp: Dispatcher):
    dp.register_message_handler(timetable, commands=['timetable'])