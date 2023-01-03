from create_bot import bot, dp
import logger
from aiogram import types, Dispatcher
from keyboards.inline import inline_delete


async def delete(callback_query: types.CallbackQuery):
    await logger.logger_cq(command="delete", call=callback_query)
    await callback_query.message.delete()

async def cat(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id, reply_markup=inline_delete, photo="https://cataas.com/cat/mlzdJ9v49C6n0bO3")

def register_handlers_commands(dp: Dispatcher):
    dp.register_message_handler(cat, commands=['random_cat'])
    dp.register_callback_query_handler(delete, text="delete")