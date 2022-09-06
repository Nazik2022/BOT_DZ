import sqlite3
from config import bot

def sql_create():
    global dp, cursor
    dp = sqlite3.connect("bot.sqlite3")
    cursor = dp.cursor()

    if dp:
        print("База данных подключенп!")
    dp.execute("CREATE TABLE IF NOT EXISTS menu ("
               "photo TEXT, name TEXT PRIMARY KEY,"
                "description TEXT, price INTEGER)"
               )

    dp.commit()

async def sql_command_insert(state):
    async with state.proxy() as date:
        cursor.execute("INSERT INTO menu VALUES"
                       "(?,?,?,?)",
                       tuple(date.values()))

        dp.commit()


