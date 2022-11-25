import os

from handlers import *

from aiogram.bot import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor


bot_token = os.getenv("TOKEN")
bot = Bot(bot_token)
dp = Dispatcher(bot)

# Регистрация обработчиков
register_message_handler(dp)
register_query_handler(dp)

executor.start_polling(dispatcher=dp, skip_updates=True)
