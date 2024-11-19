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

load_dotenv()

BOT_TOKEN = os.getenv('API_KEY')
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    text = f'Hello, {message.from_user.first_name}!'
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Joke", callback_data="joke")
        ]
    ])
    await message.answer(text, reply_markup=markup)


@dp.callback_query(lambda call: call.data == "joke")
async def get_category(call: CallbackQuery):
    text = "Select a category"
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Any", callback_data="joke_Any"),
        ],
        [
            InlineKeyboardButton(text="Programming", callback_data="joke_Programming"),
            InlineKeyboardButton(text="Misc", callback_data="joke_Misc"),
        ],
        [
            InlineKeyboardButton(text="Dark", callback_data="joke_Dark"),
            InlineKeyboardButton(text="Pun", callback_data="joke_Pun"),
        ],
        [
            InlineKeyboardButton(text="Spooky", callback_data="joke_Spooky"),
            InlineKeyboardButton(text="Christmas", callback_data="joke_Christmas"),
        ]
    ])
    await call.message.answer(text=text, reply_markup=markup)


@dp.callback_query(lambda call: call.data.startswith("joke_"))
async def send_joke(call: CallbackQuery):
    url = f"https://v2.jokeapi.dev/joke/{call.data[5:]}"
    async with aiohttp.ClientSession() as session:
        response = await session.get(url)
        json = await response.json()
    if json["type"] == "single":
        await call.message.answer(text=json["joke"])
    else:
        await call.message.answer(text=json["setup"])
        time.sleep(2)
        await call.message.answer(text=json["delivery"])


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    print("Starting...")
    asyncio.run(main())
