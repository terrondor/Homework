from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton




start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Рассчитать'),
            KeyboardButton(text='Информация'),
            KeyboardButton(text='Купить'),
            KeyboardButton(text='Регистрация')
        ]
    ], resize_keyboard=True
)

buy_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='ZMA', callback_data='buy: ZMA'),
            InlineKeyboardButton(text='Opti', callback_data='buy: Opti'),
            InlineKeyboardButton(text='Ultra', callback_data='buy: Ultra'),
            InlineKeyboardButton(text='Magne', callback_data='buy: Magne')
        ]
    ], resize_keyboard=True
)

calc_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Расчитать норму каллорий', callback_data='calories'),
            InlineKeyboardButton(text='Формула расчета', callback_data='formulas')
        ]
    ], resize_keyboard=True
)
