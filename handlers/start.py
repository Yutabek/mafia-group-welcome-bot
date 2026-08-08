from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message


router = Router()


@router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(
        "🎭 Xush kelibsiz!\n\n"
        "Guruhimizga qo‘shilganingizdan xursandmiz.\n\n"
        "O‘yinda qatnashishdan oldin guruh qoidalari "
        "bilan tanishib chiqing."
    )
