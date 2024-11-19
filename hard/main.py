import os, asyncio

from dotenv import load_dotenv

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import (Message,
                           InlineKeyboardButton,
                           InlineKeyboardMarkup,
                           CallbackQuery
                           )
from scrapper import get_links

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
            InlineKeyboardButton(text="eBay", callback_data="ebay")
        ]
    ])
    await message.answer(text, reply_markup=markup)


@dp.callback_query(lambda call: call.data == "ebay")
async def callback(call: CallbackQuery):
    user_id = call.from_user.id
    ebay_states[user_id] = True
    await call.message.answer(text=f"What do u wanna find, blud?")


@dp.message()
async def search(message: Message):
    user_id = message.from_user.id
    if ebay_states.get(user_id):
        query = message.text
        await message.answer(text="Searching...")
        try:
            links = await get_links(query)
            if links == "Error":
                await message.answer("Error, try again later")

            elif not links:

                await message.answer("Nothing found")
            else:
                text = ""
                for num, link in enumerate(links, 1):
                    text += f"{num}. [Link]({link})\n"

                await message.answer(text=text, parse_mode="Markdown")
        except Exception as e:

            print(e)
            await message.answer("Error, try again later")
        finally:
            text = "Again?"
            markup = InlineKeyboardMarkup(inline_keyboard=[
                [
                    InlineKeyboardButton(text="eBay", callback_data="ebay")
                ]
            ])
            ebay_states[user_id] = False
            await message.answer(text=text, reply_markup=markup)


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    print("Starting...")
    asyncio.run(main())
