from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


router = Router()


@router.message(CommandStart())
async def start_handler(message: Message):

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="📖 Qoidalar bilan tanishish",
                    callback_data="rules"
                )
            ]
        ]
    )

    await message.answer(
        "🎭 <b>Xush kelibsiz!</b>\n\n"
        "Guruhimizga qo‘shilganingizdan xursandmiz.\n\n"
        "O‘yinda qatnashishdan oldin guruh qoidalari "
        "bilan tanishib chiqing.",
        reply_markup=keyboard,
        parse_mode="HTML"
    )
