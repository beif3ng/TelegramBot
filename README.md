# TelegramBot

Three progressively more complex Telegram bots built with [aiogram 3](https://docs.aiogram.dev/), organized by difficulty. Each level introduces new concepts: from basic command handling to inline keyboards, external API calls, and web scraping.

## Structure

```
TelegramBot/
├── easy/       # /ping command with batch user mentions
├── medium/     # Inline keyboard bot: jokes by category
└── hard/       # Inline keyboard bot: jokes + schedule + eBay search
```

---

## Easy

A minimal bot with a single `/ping` command that mentions a predefined list of Telegram users. Mentions are sent in batches of 5 with a 1-second delay between messages to avoid Telegram's flood-wait limit.

**Concepts:** `CommandFilter`, batch iteration, `asyncio.sleep` for rate limiting.

---

## Medium

An inline keyboard bot that fetches jokes from the [JokeAPI](https://jokeapi.dev/) by category.

**Flow:**
1. `/start` → welcome message with inline keyboard
2. User taps "Joke" → category picker appears (Any, Programming, Misc, Dark, Pun, Spooky, Christmas)
3. User picks a category → bot fetches and delivers a joke via `aiohttp`

**Concepts:** `InlineKeyboardMarkup`, `CallbackQuery`, `aiohttp` async HTTP requests, `startswith` callback routing.

---

## Hard

Extends the medium bot with two additional features:

**Class schedule lookup** — the bot reads a weekly schedule (Monday–Saturday) and returns the timetable for the selected day via inline keyboard buttons.

**eBay product search** — when the user selects "eBay", the bot accepts a search query and returns up to 7 product links scraped from eBay search results using `aiohttp` + `BeautifulSoup`.

**Concepts:** stateful user tracking with a dict, `bs4` HTML parsing, multi-stage callback flows, web scraping.

---

## Getting Started

Each bot lives in its own directory with its own entry point.

### Prerequisites

- Python 3.10+
- A Telegram bot token from [@BotFather](https://t.me/BotFather)

### Installation

```bash
git clone https://github.com/beif3ng/TelegramBot.git
cd TelegramBot
pip install -r requirements.txt
```

### Configuration

Create a `.env` file in the bot directory you want to run:

```
API_KEY=your_telegram_bot_token
```

The easy bot uses `BOT_TOKEN` — check the top of `easy/main.py` for the variable name.

### Running

```bash
# Easy
python easy/main.py

# Medium
python medium/main.py

# Hard
python hard/main.py
```

## Dependencies

| Package | Used in |
|---|---|
| `aiogram` | All bots — Telegram framework |
| `aiohttp` | Medium, Hard — async HTTP |
| `beautifulsoup4` | Hard — HTML parsing for eBay |
| `python-dotenv` | All bots — env config |

## Contact

**Telegram:** [@](https://t.me/)
**Email:** 
