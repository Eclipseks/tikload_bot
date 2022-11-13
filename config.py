from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

bot=Bot('YOUR TELEGRAM API TOKEN')
dp = Dispatcher(bot, storage=MemoryStorage())

ADMIN_USER = 1033082924