from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import CommandStart

router = Router()


def get_main_menu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📚 Fanlar")],
            [KeyboardButton(text="📝 Test ishlash")],
            [KeyboardButton(text="🏆 Mening natijam")],
            [KeyboardButton(text="ℹ️ Bot haqida")]
        ],
        resize_keyboard=True
    )


@router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(
        "🎓 Assalomu alaykum!\n\n"
        "StudyMate botiga xush kelibsiz! 📚\n"
        "Men sizga dars qilish va test ishlashda yordam beraman.",
        reply_markup=get_main_menu()
    )


@router.message(F.text == "📚 Fanlar")
async def subjects_handler(message: Message):
    await message.answer(
        "📚 Fanlardan birini tanlang:\n\n"
        "🧮 Matematika\n"
        "🧬 Biologiya\n"
        "⚗️ Kimyo\n"
        "🇬🇧 Ingliz tili"
    )


@router.message(F.text == "📝 Test ishlash")
async def test_handler(message: Message):
    await message.answer(
        "📝 Test bo'limi tez orada ishga tushadi! 🚀"
    )


@router.message(F.text == "🏆 Mening natijam")
async def result_handler(message: Message):
    await message.answer(
        "🏆 Sizning natijangiz:\n\n"
        "Hozircha test ishlanmagan."
    )


@router.message(F.text == "ℹ️ Bot haqida")
async def about_handler(message: Message):
    await message.answer(
        "🎓 StudyMate — o'quvchilarga dars qilishda "
        "va test ishlashda yordam beruvchi Telegram bot."
    )
