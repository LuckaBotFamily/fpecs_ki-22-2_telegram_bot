from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import config

bot = Bot(token=config.TOKEN, parse_mode='HTML')
dp = Dispatcher(bot)