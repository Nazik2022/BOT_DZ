from aiogram import types, Dispatcher
from aiogram.types import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton

from config import dp, bot

async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_2 = InlineKeyboardButton("Next", callback_data="button_3")
    markup.add(button_2)

    question = "Какая сегодня погода"
    answers = ["Теплая", "Дождливая", "Снежная"]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=True,
        type='quiz',
        correct_option_id=0,
        explanation="Теплее",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup
    )


async def quiz_3(call: types.CallbackQuery):

    question = "Что у нас сегодня на ужин?"
    answers = ["Лагман", "Плов", "Манты", "Дымдама", "Ганфан"]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=True,
        type='quiz',
        correct_option_id=2,
        explanation="Их много",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
    )


def register_callback_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, lambda call: call.data == "button_2")
    dp.register_callback_query_handler(quiz_3, lambda call: call.data == "button_3")