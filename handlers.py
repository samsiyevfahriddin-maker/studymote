from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from database import add_user

router = Router()


@router.message(CommandStart())
async def start_handler(message: Message):
    add_user(
        message.from_user.id,
        message.from_user.username,
        message.from_user.first_name
    )

    builder = ReplyKeyboardBuilder()

    builder.button(text="📚 Darslar")
    builder.button(text="📝 Testlar")
    builder.button(text="📊 Natijam")
    builder.button(text="ℹ️ Bot haqida")

    builder.adjust(2)

    await message.answer(
        f"Salom, {message.from_user.first_name}! 👋\n\n"
        "🎓 StudyMate botiga xush kelibsiz!\n\n"
        "Bu bot orqali darslarni o‘rganish, test ishlash "
        "va natijalarni ko‘rish mumkin.",
        reply_markup=builder.as_markup(resize_keyboard=True)
    )


@router.message()
async def message_handler(message: Message):
    if message.text == "📚 Darslar":
        await message.answer(
            "📚 Darslar bo‘limi\n\n"
            "Bu yerda fanlar bo‘yicha darslarni o‘rganishingiz mumkin."
        )

    elif message.text == "📝 Testlar":
        await message.answer(
            "📝 Testlar bo‘limi\n\n"
            "Hozircha testlar tayyorlanmoqda. 🚀"
        )

    elif message.text == "📊 Natijam":
        await message.answer(
            "📊 Natijangiz\n\n"
            "Hozircha sizda test natijalari mavjud emas."
        )

    elif message.text == "ℹ️ Bot haqida":
        await message.answer(
            "ℹ️ StudyMate — o‘quvchilarga darslarni "
            "o‘rganish va test ishlashda yordam beruvchi Telegram bot."
        )

    else:
        await message.answer(
            "🤔 Men bu buyruqni tushunmadim.\n"
            "Pastdagi tugmalardan birini tanlang."
        )
