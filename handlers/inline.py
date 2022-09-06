

# import hashlib
# from aiogram import types, Dispatcher
#
#
#
# async def inline_google_handler(query: types.InlineQuery):
#     text = query.query or "echo"
#     link = f"https://www.google.ru{text}"
#     articles = [types.InlineQueryResultArticle(
#         id=heshlib.md5(text.encode()).hexdigest(),
#         title="Googl:",
#         url=link,
#         input_message_content=types
#
#
#
#
# def register_handlers_inline(dp: Dispatcher):
#     dp.register_inline_handler(inline_google_handler)