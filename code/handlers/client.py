from get_file_text import get_file_text

from aiogram import types


# Обработчик Inline-кнопок
async def callback_query_handler(callback: types.CallbackQuery):
    # Социальные сети
    if callback.data == "socials":
        msg = get_file_text("texts/socials.txt")

        # Клавиатура для сообщения бота
        keyboard = types.InlineKeyboardMarkup()

        without_protocol_btn = types.InlineKeyboardButton(text="Показать без «https://»",
                                                          callback_data="without_protocol")
        back_btn = types.InlineKeyboardButton(text="Назад", callback_data="back")

        keyboard.add(without_protocol_btn, back_btn)

        await callback.message.edit_text(msg, reply_markup=keyboard)

    # Вернуться в главное меню
    elif callback.data == "back":
        answer_text = get_file_text("texts/start.txt")

        # Клавиатура для сообщения бота
        keyboard = types.InlineKeyboardMarkup()

        socials_btn = types.InlineKeyboardButton(text="Соц. сети", callback_data="socials")
        link_btn = types.InlineKeyboardButton(text="Ссылка на бота", callback_data="link")

        keyboard.add(socials_btn, link_btn)

        await callback.message.edit_text(text=answer_text, reply_markup=keyboard)

    # Показать ссылки на социальные сети без протокола
    elif callback.data == "without_protocol":
        answer_text = get_file_text("texts/without_protocol.txt")

        # Клавиатура для сообщения бота
        keyboard = types.InlineKeyboardMarkup()

        socials_btn = types.InlineKeyboardButton(text="Показать c «https://»", callback_data="socials")
        link_btn = types.InlineKeyboardButton(text="В главное меню", callback_data="back")

        keyboard.add(socials_btn, link_btn)

        await callback.message.edit_text(text=answer_text, reply_markup=keyboard)

    # Показать ссылки на бота
    elif callback.data == "link":
        answer_text = get_file_text("texts/bot_link.txt")

        # Клавиатура для сообщения бота
        keyboard = types.InlineKeyboardMarkup(row_width=1)

        socials_btn = types.InlineKeyboardButton(text="Cоц. Сети", callback_data="socials")
        without_social_btn = types.InlineKeyboardButton(text="Cоц. Сети без протокола",
                                                        callback_data="without_protocol")
        back = types.InlineKeyboardButton(text="В главное меню", callback_data="back")

        keyboard.add(socials_btn, back, without_social_btn)

        await callback.message.edit_text(text=answer_text, reply_markup=keyboard)
