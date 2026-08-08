from aiogram import Router
from aiogram.types import (
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from aiogram.utils.markdown import html_decoration


router = Router()


@router.message()
async def new_member_handler(message: Message):
    if not message.new_chat_members:
        return

    for user in message.new_chat_members:
        mention = f'<a href="tg://user?id={user.id}">🎭</a>'

        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text="📖 Qoidalar bilan tanishish",
                        url="https://t.me/MafiaGroupWelcomeBot?start=rules"
                    )
                ]
            ]
        )

        await message.answer(
            f"🎭 {mention} <b>guruhimizga xush kelibsiz!</b>\n\n"
            "O‘yinda qatnashishdan oldin guruh qoidalari "
            "bilan tanishib chiqing.",
            reply_markup=keyboard,
            parse_mode="HTML",
        )
