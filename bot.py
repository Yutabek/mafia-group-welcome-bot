import asyncio

from aiogram import Bot, Dispatcher

from config import BOT_TOKEN
from handlers.start import router as start_router
from handlers.rules import router as rules_router
from handlers.welcome import router as welcome_router


dp = Dispatcher()

dp.include_router(start_router)
dp.include_router(rules_router)
dp.include_router(welcome_router)


async def main():
    bot = Bot(token=BOT_TOKEN)

    print("Bot ishga tushdi...")

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())
