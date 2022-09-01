from aiogram.types import KeyboardButton,ReplyKeyboardMarkup

cancel_button = KeyboardButton("CANCEL")
cancel_button =ReplyKeyboardMarkup(
    resize_keyboard=True,

).add(cancel_button)
names_1 = KeyboardButton("пицца")
names_2 = KeyboardButton("суши")
names_3 = KeyboardButton("манты")
names_4 = KeyboardButton("бургер")
names_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard= True)
names_markup.row(names_1,names_2,names_3)





