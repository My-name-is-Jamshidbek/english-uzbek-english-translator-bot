from aiogram import executor
from loader import bot
from config import ADMIN_ID
from datetime import datetime

async def on_shutdown(dp):
    text = f"""
            Salom admin.
bot ishdan toxtadi!
server vaqti: {datetime.now()}
        """
    await bot.send_message(ADMIN_ID, text)
    await bot.close()

async def on_startup(dp):
    text = f"""
            Salom admin.
bot ishga tushdi!
server vaqti: {datetime.now()}
        """
    await bot.send_message(ADMIN_ID,text)
if __name__=='__main__':
    from app import dp
    executor.start_polling(dp,on_startup=on_startup,on_shutdown=on_shutdown)