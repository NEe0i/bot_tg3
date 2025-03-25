import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command

TOKEN = "7698830417:AAEF8C9EopiACNv3pBdvwxlIboJUqdn2ZnM"

bot = Bot(token=TOKEN)
dp = Dispatcher()

logging.basicConfig(level=logging.INFO)

zodiacs = [
    "♈ Овен", "♉ Телец", "♊ Близнецы", "♋ Рак",
    "♌ Лев", "♍ Дева", "♎ Весы", "♏ Скорпион",
    "♐ Стрелец", "♑ Козерог", "♒ Водолей", "♓ Рыбы"
]

keyboard = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text=zodiac)] for zodiac in zodiacs],
    resize_keyboard=True
)


@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Выбери знак зодиака", reply_markup=keyboard)


async def get_horoscope(sign):
    question = f"Расскажи гороскоп для знака {sign} на сегодня"
    response = await ask_chatgpt(question)
    return response


# Запрос к ChatGPT
async def ask_chatgpt(question):
    response = await asyncio.to_thread(lambda: "⏳" + question)
    return response  # Здесь можно заменить на API-запрос


# Обработчик выбора знака зодиака
@dp.message()
async def zodiac_selected(message: types.Message):
    sign = message.text.strip()
    if sign in zodiacs:
        horoscope = await get_horoscope(sign)
        await message.answer(horoscope)
    else:
        await message.answer("Пожалуйста, выбери знак зодиака из списка.")


# Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
