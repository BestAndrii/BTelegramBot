from .client import callback_query_handler
from .start import start

from aiogram.dispatcher import Dispatcher


# Регистрация обработчика callback
def register_query_handler(dp: Dispatcher):
    dp.register_callback_query_handler(callback_query_handler)


# Регистрация обработчика message handler
def register_message_handler(dp: Dispatcher):
    dp.register_message_handler(start)
