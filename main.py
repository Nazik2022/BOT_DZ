from aiogram.utils import executor
from config import dp
from handlers import extra, client, callback, fsmAdminMenu, notification, inline
from databace import bot_dp
import asyncio


async def on_startup(_):
    asyncio.create_task(notification.scheduler())
    bot_dp.sql_create()


fsmAdminMenu.register_handlers_fsmAdminMenu(dp)
notification.register_handlers_notification(dp)
client.register_client_handlers(dp)
callback.register_callback_handlers(dp)
extra.register_extra_handlers(dp)
inline.register_handlers_inline(dp)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
