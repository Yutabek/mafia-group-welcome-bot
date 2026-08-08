from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import (
    Message,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)


router = Router()


@router.message(CommandStart())
async def start_handler(message: Message):
    args = message.text.split(maxsplit=1)

    if len(args) > 1 and args[1] == "rules":
        from handlers.rules import RULES_TEXT

        await message.answer(
            RULES_TEXT,
            parse_mode="HTML",
        )
        return

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="📖 Qoidalar bilan tanishish",
                    callback_data="rules",
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
        parse_mode="HTML",
    )
