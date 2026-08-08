import asyncio
import os

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
from dotenv import load_dotenv


load_dotenv()

BOT_TOKEN = os.getenv(8316292761:AAET6f_wIs4aEoBCuPVkA20san0JtA68KGQ)

dp = Dispatcher()


@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(
        "🎭 Xush kelibsiz!\n\n"
        "Guruhimizga qo‘shilganingizdan xursandmiz.\n\n"
        "O‘yinda qatnashishdan oldin guruh qoidalari "
        "bilan tanishib chiqing."
    )


async def main():
    if not BOT_TOKEN:
        raise ValueError("BOT_TOKEN topilmadi!")

    bot = Bot(token=BOT_TOKEN)

    print("Bot ishga tushdi...")

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
