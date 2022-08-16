from aiogram import types, Dispatcher
from confing import dp, bot, ADMIN
import random

async def game(message: types.Message):
    if message.text.startswith('game') and message.from_user.id in ADMIN:
        emojis = ['⚽', '🏀', '🎰', '🎯', '🎳', '🎲']
        emoji = random.choice(emojis)
        await bot.send_dice(message.chat.id, emoji=emoji)
    else:
        await bot.send_message(message.chat.id, "Эта команда работает только для АДМИНА!!!")

def register_admin_handlers(dp: Dispatcher):
    dp.register_message_handler(game)
