from aiogram import Router, F
from aiogram.types import CallbackQuery


router = Router()


RULES_TEXT = """
📜 <b>GURUH QOIDALARI</b>

1. 🤝 Barcha ishtirokchilarga hurmat bilan munosabatda bo‘ling.

2. 🚫 Reklama va spam taqiqlanadi.

3. 🔗 Boshqa guruh yoki kanallarga odamlarni jalb qilish taqiqlanadi.

4. 🎭 O‘yin davomida boshqa o‘yinchilarning shaxsiy ma'lumotlarini
tarqatmang.

5. ⚠️ Adminlar ko‘rsatmalariga amal qiling.

6. 🎮 O‘yin jarayonida umumiy guruh qoidalariga rioya qiling.

Qoidalarni buzish ogohlantirish yoki guruhdan chiqarilishiga
olib kelishi mumkin.
"""


@router.callback_query(F.data == "rules")
async def rules_handler(callback: CallbackQuery):
    await callback.message.edit_text(
        RULES_TEXT,
        parse_mode="HTML",
    )

    await callback.answer()
