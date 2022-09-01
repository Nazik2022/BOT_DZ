from aiogram import types, Dispatcher
from confing import dp, bot
import random


async def echo(message: types.Message):
    if message.text.startswith('game') and message.from_user.id in ADMIN:
        emojis = ['⚽', '🏀', '🎰', '🎯', '🎳', '🎲']
        emoji = random.choice(emojis)
        await bot.send_dice(message.chat.id, emoji=emoji)
    elif message.text.isdigit():
        k = int(message.text)
        k *= k
        await bot.send_message(message.chat.id, k)
    else:
        await bot.send_message(message.from_user.id, message.text)

def register_extra_handlers(dp: Dispatcher):
    dp.register_message_handler(echo)



