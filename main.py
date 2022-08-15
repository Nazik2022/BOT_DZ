from aiogram.utils import executor
from confing import dp

from handlers import admin, extra, client, callback

admin.register_admin_handlers(dp)
client.register_client_handlers(dp)
callback.register_callback_handlers(dp)
extra.register_extra_handlers(dp)


if __name__=="__main__":
    executor.start_polling(dp, skip_updates=True)