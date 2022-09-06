import asyncio
import aioschedule
from aiogram import types, Dispatcher
from config import bot


async def get_chat_id(message: types.Message):
    global chat_id
    chat_id = message.from_user.id
    await bot.send_message(chat_id=chat_id, text="ok!")

async def sports_activities():
    await bot.send_message(chat_id=chat_id, text="на пробежку")



async def scheduler():
    aioschedule.every().wednesday.at("19:32").do(sports_activities)

    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)

def register_handlers_notification(dp: Dispatcher):
    dp.register_message_handler(get_chat_id,
                                lambda word: 'напомни' in word.text)

