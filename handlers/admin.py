from aiogram import types, Dispatcher
from confing import dp, bot, ADMIN
import random

async def game(message: types.Message):
    pass

def register_admin_handlers(dp: Dispatcher):
    dp.register_message_handler(game)
