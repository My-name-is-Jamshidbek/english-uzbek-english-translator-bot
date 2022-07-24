from aiogram.types import ReplyKeyboardMarkup,KeyboardButton



#kontaktni olish uchun butoon
keyboard_kontakt = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_kontakt.add(KeyboardButton(text="kontaktni ulashish", request_contact=True))

'''
quyidagilar admin  uchun
'''
keyboard_admin_menu_1 = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_admin_menu_1.add(
    KeyboardButton(text='Reklama berish'),
)

keyboard_admin_rozibolish = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_admin_rozibolish.add(
    KeyboardButton(text='Tasdiqlash'),
    KeyboardButton(text='Bekor qilish'),
)