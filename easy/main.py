import asyncio
import os
import aiohttp
import time

from dotenv import load_dotenv

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import (Message,
                           InlineKeyboardButton,
                           InlineKeyboardMarkup,
                           CallbackQuery
                           )

from schedule import get_schedule

load_dotenv()

BOT_TOKEN = os.getenv('API_KEY')
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
ebay_states = {}


@dp.message(CommandStart())
async def start(message: Message):
    text = f'Hello, {message.from_user.first_name}!'
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Schedule", callback_data="schedule"),
            InlineKeyboardButton(text="Joke", callback_data="joke"),
        ],
        [
            InlineKeyboardButton(text="eBay", callback_data="ebay"),
        ]
    ])
    await message.answer(text, reply_markup=markup)


@dp.callback_query(lambda call: call.data == "schedule")
async def get_answer(call: CallbackQuery):
    text = f'Wanna know schedule?'
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Mon", callback_data="Mon"),
            InlineKeyboardButton(text="Tue", callback_data="Tue"),
        ],
        [

            InlineKeyboardButton(text="Wed", callback_data="Wed"),
            InlineKeyboardButton(text="Thu", callback_data="Thu"),
        ],
        [
            InlineKeyboardButton(text="Fri", callback_data="Fri"),
            InlineKeyboardButton(text="Sat", callback_data="Sat"),
        ]
    ])
    await call.message.answer(text=text, reply_markup=markup)


@dp.callback_query(lambda call: call.data in ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat"])
async def send_schedule(call: CallbackQuery):
    schedule_text = get_schedule(call.data)
    await call.message.answer(text=schedule_text)


@dp.callback_query(lambda call: call.data == "ebay")
async def callback(call: CallbackQuery):
    user_id = call.from_user.id
    ebay_states[user_id] = True
    await call.message.answer(text=f"What do u wanna find, blud?")


@dp.message()
async def callback(message: Message):
    user_id = message.from_user.id
    if ebay_states.get[user_id]:
        query = message.text
        await message.answer(text="Searching")


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    print("Starting...")
    asyncio.run(main())
