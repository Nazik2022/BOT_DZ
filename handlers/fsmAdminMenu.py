from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from confing import bot
from handlers.keyboards.client_kb import names_markup
from databace import bot_dp


class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()
    
async def fsm_start(message: types.Message):
    if message.chat.type == "private":
        await FSMAdmin.photo.set()
        await message.answer(f"Здраствуйте{message.from_user.full_name} \n"
                             f"отправте фото")
                             # reply_markup=cancel_markup)

async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
    await FSMAdmin.next()
    await message.answer("Название блюда", reply_markup=names_markup)


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMAdmin.next()
    await message.answer("Состав блюда:")

async def load_description(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text
    await FSMAdmin.next()
    await message.answer("Цены на блюда")

async def load_price(message: types.Message, state: FSMContext):
    try:
        if int(message.text) <= 5000:
            async with state.proxy() as data:
                data['price'] = message.text
                await bot.send_photo(message.from_user.id, data['photo'],
                                     caption=f"Name: {data['name']}\n"
                                             f"description: {data['description']}\n"
                                             f"price: {data['price']}")

            await bot_dp.sql_command_insert(state)
            await state.finish()
        else:
            await message.answer("Введи другую сумму")
    except ValueError:
        await message.answer("Пиши числа!")
        # print(data)


def register_handlers_fsmAdminMenu(dp: Dispatcher):
    dp.register_message_handler(fsm_start, commands=["menu"])
    dp.register_message_handler(load_photo, state=FSMAdmin.photo, content_types=['photo'])
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_description, state=FSMAdmin.description)
    dp.register_message_handler(load_price, state=FSMAdmin.price)











