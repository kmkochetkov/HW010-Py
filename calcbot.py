import aiogram

import time
import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils import executor

TOKEN = "5865547215:AAFn5uB_1sWExB5pfSg29xJhkH02dMNAwdA"

bot = Bot(token = TOKEN)
dp = Dispatcher(bot)


@dp.message_handler()
async def get_message(message: types.Message):
    chat_id = message.chat.id
    text = message.text
    filterred = list(filter(lambda x: 'абв' not in x, text.split()))

    await message.answer(f'{" ".join(filterred)}')


executor.start_polling(dp)