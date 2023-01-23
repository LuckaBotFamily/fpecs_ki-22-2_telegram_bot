from create_bot import bot, dp
import logger
from aiogram import types, Dispatcher
from keyboards.inline import inline_delete


async def delete(callback_query: types.CallbackQuery):
    await logger.logger_cq(command="delete", call=callback_query)
    await callback_query.message.delete()

async def cat(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id, reply_markup=inline_delete, photo="https://cataas.com/cat/mlzdJ9v49C6n0bO3")

async def help(message: types.Message):
    text = """
== Щоденний розклад ==
    /today - розклад на сьогодні
    /tommorow - розклад на завтра
    /monday - розклад на понеділок
    /tuesday - розклад на вівторок
    /wednesday - розклад на середу
    /thursday - розклад на четвер
    /friday - розклад на п'ятницю
    
== Повний розклад ==
    /timetable [-|full] - розклад на весь тиждень у малому або великому форматі
    
==Повідомлення==
    /notify [on|of] - включити або виключити повідомлення о початку пари
    
Якщо у вас є якісь побажання чи проблеми пишіть у особисті повідомлення > @luckyakalucka
    """

    await bot.send_message(chat_id=message.chat.id, text=text)
    await logger.logger_mess(message)
def register_handlers_commands(dp: Dispatcher):
    dp.register_message_handler(cat, commands=['random_cat'])
    dp.register_message_handler(help, commands=['help'])
    dp.register_callback_query_handler(delete, text="delete")