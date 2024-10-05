from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

api = "7426305553:AAEGpI0EYLblIEfa3ZmhsjI6whniCvC7468"

bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


kb = ReplyKeyboardMarkup(resize_keyboard=True)
button = KeyboardButton(text='Расчитать')
button_2 = KeyboardButton(text='Информация')
button_3 = KeyboardButton(text='Купить')
kb.add(button).add(button_2).add(button_3)

inline_kb = InlineKeyboardMarkup(row_width=1)
products_buttons = [
    InlineKeyboardButton(text='Product1', callback_data='buy:1'),
    InlineKeyboardButton(text='Product2', callback_data='buy:2'),
    InlineKeyboardButton(text='Product3', callback_data='buy:3'),
    InlineKeyboardButton(text='Product4', callback_data='buy:4'),
]
inline_kb.add(*products_buttons)

inline_kb_calculate = InlineKeyboardMarkup(row_width=1)
calculate_buttons = [
    InlineKeyboardButton(text='Расчитать норму каллорий', callback_data='calories'),
    InlineKeyboardButton(text='Формула расчета', callback_data='formulas'),
]
inline_kb_calculate.add(*calculate_buttons)


@dp.message_handler(commands=['start'])
async def main_menu(message: types.Message):
    await message.answer('Привет! Я посчитаю норму ваших калорий в день. Выберите опцию.', reply_markup=kb)

@dp.message_handler(text='Информация')
async def info(message):
    with open('main.jpeg', 'rb') as f:
        await message.answer_photo(f, 'Вас приветствует бот, с моей помощью вы можете купить витамины а также расчитать норму калорий')

@dp.message_handler(text='Расчитать')
async def calculate_menu(message: types.Message):
    await message.answer("Выберите опцию:", reply_markup=inline_kb_calculate)


@dp.message_handler(text='Купить')
async def get_buying_list(message: types.Message):
    products_info = [
        ("Product1", "ZMA", 1125),
        ("Product2", "Opti", 2504),
        ("Product3", "Ultra", 2561),
        ("Product4", "Magne", 500),
    ]
    for product in products_info:
        name, description, price = product
        response_text = f"Название: {name} | Описание: {description} | Цена: {price}\n"
        image_path = f"images/{name}.jpg"
        with open(image_path, 'rb') as img:
            await message.answer_photo(img, caption=response_text)

    await message.answer("Выберите продукт для покупки:", reply_markup=inline_kb)


@dp.callback_query_handler(lambda call: call.data.startswith('buy:'))
async def send_confirm_message(call: types.CallbackQuery):
    product_id = call.data.split(':')[1]
    await call.answer()
    await call.message.answer(f"Вы успешно приобрели продукт {product_id}!")


@dp.callback_query_handler(text='formulas')
async def get_formulas(call: types.CallbackQuery):
    await call.answer()
    formula_text = ("Формула Миффлина-Сан Жеора:\n"
                    "Для мужчин: BMR = 10 * вес(кг) + 6.25 * рост(см) - 5 * возраст(лет) + 5\n"
                    "Для женщин: BMR = 10 * вес(кг) + 6.25 * рост(см) - 5 * возраст(лет) - 161")
    await call.message.answer(formula_text)


@dp.callback_query_handler(text='calories')
async def set_age(call: types.CallbackQuery):
    await call.answer()
    await call.message.answer("Введите ваш возраст:")
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)
    await UserState.growth.set()
    await message.answer("Введите ваш рост в сантиметрах:")


@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    await state.update_data(growth=message.text)
    await UserState.weight.set()
    await message.answer("Введите ваш вес в килограммах:")


@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    age = int(data["age"])
    growth = int(data["growth"])
    weight = int(data["weight"])

    bmr = 10 * weight + 6.25 * growth - 5 * age + 5
    await message.reply(f"Ваша норма калорий: {bmr} ккал в день.")

    await state.finish()


if __name__=="__main__":
    executor.start_polling(dp, skip_updates=True)
