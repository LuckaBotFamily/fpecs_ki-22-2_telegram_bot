from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

inline_delete = InlineKeyboardMarkup().add(InlineKeyboardButton('❌', callback_data='delete'))

list = InlineKeyboardMarkup().add(
    InlineKeyboardButton('◀', callback_data='left'),
    InlineKeyboardButton('🔶/🔷', callback_data='change'),
    InlineKeyboardButton('▶', callback_data='right'))