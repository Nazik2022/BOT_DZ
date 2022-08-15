from aiogram import types, Dispatcher
from confing import dp, bot


async def echo(message: types.Message):
    if message.text.isdigit():
        k = int(message.text)
        k *= k
        await bot.send_message(message.chat.id, k)
    else:
        await bot.send_message(message.from_user.id, message.text)

def register_extra_handlers(dp: Dispatcher):
    dp.register_message_handler(echo)