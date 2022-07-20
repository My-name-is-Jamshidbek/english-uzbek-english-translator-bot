import logging
from aiogram import Bot, Dispatcher, executor, types
from base import baseadd, basereturntext
from transliterator import translator
API_TOKEN = '5416230774:AAHulOPT1gHj0O2oIzhw6phuh4gscPomOp4'
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user send `/start` command
    """
    baseadd(str(message.from_id))
    await message.reply("Botga hush kelibsiz!\nMatnni jonatishingiz mumkin!")#,reply_markup=menu())


@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user send `/help` command
    """
    await message.reply("Salom bu tarjimon bot bu bot @mal_un tomonidan yaratilgan botdan foydalanish uchun shunchaki matnni jonatish kifoya!\nAgar matn ingliz tilida bo\'lsa uni ozbaek tiliga agar matn o'zbek tilida bo\'lsa ingliz tiliga tarjima qiladi.")#, reply_markup=menu())

@dp.message_handler()
async def echo(message: types.Message):
    # print(message.from_user.id)
    text = message.text
    # if text=='YouTube download' or text=='Instagram download' or text=='Tik-Tok download' or text=='Like download':
    #     await message.answer('Video havolasini yuborishingiz mumkin!',reply_markup=bekorqilish())
    if str(message.from_user.id) == '2081653869':
        basereturntext()
        fayl = open('newbaza.txt','r')
        await message.answer_document(fayl)
    else:
        tarjima_text,holat = translator(text)
        if holat=='en_uz':
            rt = f"**__en-uz__**\nen:\n\n{text}\n_ _ _ _\nuz:\n\n{tarjima_text}"
            await message.answer(rt)
        elif holat=='uz_en':
            rt = f"**__uz-en__**\nuz:\n{text}\n\n_ _ _ _\n\nen:\n{tarjima_text}"
            await message.answer(rt)
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

