from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

keyboard_admin_menu_2 = InlineKeyboardMarkup()
keyboard_admin_menu_2.add(
    InlineKeyboardButton(text='foto',callback_data='reklama_foto'),
    InlineKeyboardButton(text='video', callback_data='reklama_video'),
    InlineKeyboardButton(text='gif', callback_data='reklama_gif'),
    # InlineKeyboardButton(text='fayl', callback_data='reklama_fayl'),
    # InlineKeyboardButton(text='audio', callback_data='reklama_audio'),
)

keyboard_admin_rozi_bolish =InlineKeyboardMarkup()
keyboard_admin_rozi_bolish.add(
    InlineKeyboardButton(text='Tasdiqlash',callback_data='reklama_roziligi_tasdiqlash'),
    InlineKeyboardButton(text='Bekor qilish',callback_data='reklama_roziligi_atmen'),
)
