from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import crud_function
import asyncio

from config import *
from keyboard import *
from text import *


bot = Bot(token=API)
dp = Dispatcher(bot, storage=MemoryStorage())


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(commands=['start'])
async def main_menu(message: types.Message):
    await message.answer(f'{start_text}', reply_markup=start_kb)


@dp.message_handler(text='Информация')
async def info(message):
    with open('main.jpeg', 'rb') as f:
        await message.answer_photo(f, f'{info_text}', reply_markup=start_kb)


@dp.message_handler(text='Рассчитать')
async def calculate_menu(message: types.Message):
    await message.answer(f'{calc_text}', reply_markup=calc_kb)


@dp.message_handler(text=['Регистрация'])
async def register(message: types.Message):
    await message.answer(f'{reg_text}', reply_markup=start_kb)
    await RegistrationState.username.set()


@dp.message_handler(text='Купить')
async def get_buying_list(message: types.Message):
    products_info = crud_function.get_all_products()

    if not products_info:
        await message.answer("Нет доступных продуктов!")
        return
    else:
        for product in products_info:
            _, name, description, price = product
            response_text = f"Название: {name} | Описание: {description} | Цена: {price}\n"

            image_path = f"images/{name}.jpg"
            try:
                with open(image_path, 'rb') as img:
                    await message.answer_photo(img, caption=response_text)
            except FileNotFoundError:
                await message.answer(response_text)  # Показываем текст, если изображения нет

    await message.answer("Выберите продукт для покупки:", reply_markup=buy_kb)


@dp.callback_query_handler(lambda call: call.data.startswith('buy:'))
async def send_confirm_message(call: types.CallbackQuery):
    product_id = call.data.split(':')[1]
    await call.answer()
    await call.message.answer(f"Вы успешно приобрели продукт {product_id}!")


@dp.callback_query_handler(text='formulas')
async def get_formulas(call: types.CallbackQuery):
    await call.answer()
    formula_text = f'{calc_formula}'
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


class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()
    balance = State()


@dp.message_handler(text=['register'])
async def register(message: types.Message):
    await message.answer(f"{reg_text}")
    await RegistrationState.username.set()


@dp.message_handler(state=RegistrationState.username)
async def set_username(message: types.Message, state: FSMContext):
    username = message.text.strip()

    if crud_function.is_included(username):
        await message.answer("Пользователь существует, введите другое имя")
        await RegistrationState.username.set()
        return
    await state.update_data(username=username)
    await RegistrationState.email.set()
    await message.answer("Введите ваш email:")


@dp.message_handler(state=RegistrationState.email)
async def set_email(message: types.Message, state: FSMContext):
    email = message.text.strip()
    await state.update_data(email=email)
    await RegistrationState.age.set()
    await message.answer("Введите свой возраст:")


@dp.message_handler(state=RegistrationState.age)
async def set_age(message: types.Message, state: FSMContext):
    age = message.text.strip()
    await state.update_data(age=age)

    user_data = await state.get_data()
    username = user_data.get('username')
    email = user_data.get('email')

    crud_function.add_user(username, email, age)
    await message.answer(f"Вы успешно зарегистрированы!")

    await state.update_data(balance=1000)
    await state.finish()


if __name__=='__main__':
    executor.start_polling(dp, skip_updates=True)

