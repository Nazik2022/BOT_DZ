from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ParseMode

from config import bot, dp

async def quiz(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton("Next", callback_data="button_2")
    markup.add(button_1)


    question = "Сколько человек в нашей группе?"
    answers = ["11", "10", "5", "7"]
    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=answers,
        is_anonymous=True,
        type='quiz',
        correct_option_id=1,
        explanation="Четное число",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup
    )

async def mem(message: types.Message):
    photo = open("media/photo_1.png", "rb")
    await bot.send_photo(message.chat.id, photo=photo)

async def pin(message: types.Message):
    if message.reply_to_message:
        await bot.pin_chat_message(message.chat.id, message.reply_to_message.message_id)
    else:
        await bot.send_message(message.chat.id, "Команда работает при ответе на сообщение!!!")

def register_client_handlers(dp: Dispatcher):
    dp.register_message_handler(quiz, commands=['quiz'])
    dp.register_message_handler(mem, commands=['mem'])
    dp.register_message_handler(pin, commands=['pin'], commands_prefix = ['!'])