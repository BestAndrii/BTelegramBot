from get_file_text import get_file_text
from aiogram import types


async def start(message: types.Message):
    """Ответ на любое сообщение пользователя."""
    answer_text = get_file_text("texts/start.txt")

    # Клавиатура для сообщения бота
    keyboard = types.InlineKeyboardMarkup()

    socials_btn = types.InlineKeyboardButton(text="Соц. сети", callback_data="socials")
    link_btn = types.InlineKeyboardButton(text="Ссылка на бота", callback_data="link")

    keyboard.add(socials_btn, link_btn)

    await message.answer(answer_text, reply_markup=keyboard)
