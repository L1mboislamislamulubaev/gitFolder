
from aiogram import Dispatcher, Bot
import logging

from aiogram.contrib.fsm_storage.memory import MemoryStorage

#   5465307409:AAFkG5AlqfiVZ6YR8Trfv_NGc20_I7UPhhw
bot = Bot(token='6586823928:AAHnzJE4v7czKflbZBL6eMX9JL0sqXZ5GxQ', parse_mode='HTML')
dp = Dispatcher(bot, storage=MemoryStorage())
logging.basicConfig(level=logging.INFO)