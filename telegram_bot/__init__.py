from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher, filters
from aiogram.utils import executor

from parser_utils import BaneksParser
from telegram_bot.config import TOKEN
from telegram_bot.keyboard import bot_kb

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

baneks_parser = BaneksParser()


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await bot.send_message(message.chat.id, f'Здарова, {message.from_user.first_name}! '
                                            f'Я бот с анеками на любой вкус.\n'
                                            f'Чтобы разобраться с функционалом,\n'
                                            f'пропиши /help или нажми кнопку "Помощь".',
                           reply_markup=bot_kb)


@dp.message_handler(filters.Text(equals='Помощь', ignore_case=True), state='*')
@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await bot.send_message(message.chat.id, 'Я могу рассказать случайный анекдот,\n'
                                            'либо вывести топ анекдотов.\n'
                                            'Пиши соотвественно: "Случайный анек" или "Топ анеков".',
                           reply_markup=bot_kb)


@dp.message_handler(filters.Text(equals='Случайный анек', ignore_case=True), state='*')
async def process_random_joke(message: types.Message):
    await bot.send_message(message.chat.id, baneks_parser.find_joke(),
                           reply_markup=bot_kb)


@dp.message_handler(filters.Text(equals='Топ анеков', ignore_case=True), state='*')
async def process_random_joke(message: types.Message):
    await bot.send_message(message.chat.id, 'Ещё в разработке. Пни @Bomjgangster, чтобы ускорить разработку.',
                           reply_markup=bot_kb)


def run():
    executor.start_polling(dp)
