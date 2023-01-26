from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

inline_delete = InlineKeyboardMarkup().add(InlineKeyboardButton('❌', callback_data='delete'))
inline_acceptVoice = InlineKeyboardMarkup().add(InlineKeyboardButton('✅ 🇺🇦', callback_data='acceptVoice_Ua'), InlineKeyboardButton('✅ 🇷🇺', callback_data='acceptVoice_Ru'))


list = InlineKeyboardMarkup().add(
    InlineKeyboardButton('◀', callback_data='left'),
    InlineKeyboardButton('❌', callback_data='delete'),
    InlineKeyboardButton('▶', callback_data='right'))