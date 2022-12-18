from . import slot, tools, blackred
from aiogram import types, Dispatcher

def register_handlers_games(dp: Dispatcher):
    dp.register_message_handler(slot.slot, commands=['slot'])
    dp.register_message_handler(blackred.blackred, commands=['roll'])
    dp.register_message_handler(tools.casino, commands=['casino'])
    dp.register_message_handler(tools.balance, commands=['balance'])
    dp.register_message_handler(tools.addmoney, commands=['give'])