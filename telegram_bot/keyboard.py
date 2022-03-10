from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

bot_kb = ReplyKeyboardMarkup(resize_keyboard=True)

button_random = KeyboardButton('Случайный анек')
button_top = KeyboardButton('Топ анеков')
button_help = KeyboardButton('Помощь')

bot_kb.row(button_random, button_top)
bot_kb.row(button_help)
