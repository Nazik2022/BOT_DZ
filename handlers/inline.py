import hashlib
from aiogram import types, Dispatcher


async def inline_google_handler(query: types.InlineQuery):
     text = query.query or "echo"
     link = f"https://www.google.ru{text}"
     articles = [types.InlineQueryResultArticle(
         id=hashlib.md5(text.encode()).hexdigest(),
         title= "Googl:",
         url=link,
         input_message_content=types.InputMessageContent(
             message_text=link
         )
     )]
     await query.answer(articles,cache_time=1)


 def register_handlers_inline(dp: Dispatcher):
     dp.register_inline_handler(inline_google_handler)

