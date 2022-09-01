from aiogram.utils import executor
from confing import dp

from handlers import admin, extra, client, callback, fsmAdminMenu, notification
from databace import bot_dp
import asyncio


async def on_startup(_):
    asyncio.create_task(notification.scheduler())
    # bot_dp.sql_create()

# fsmAdminMenu.register_handlers_fsmAdminMenu(dp)
notification.register_handlers_notification(dp)
client.register_client_handlers(dp)
callback.register_callback_handlers(dp)
extra.register_extra_handlers(dp)
admin.register_admin_handlers(dp)

if __name__=="__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
