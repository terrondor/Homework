from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup, default_state
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import asyncio

from main import button2


api = " "

bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup(resize_keyboard=True)
button = KeyboardButton(text='Расчитать')
button_2 = KeyboardButton(text='Информация')
kb.add(button)
kb.add(button_2)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(text="Расчитать")
async def set_age(message):
    await message.answer("Введите ваш возраст:")
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)
    await UserState.growth.set()
    await message.answer("Введите ваш рост в сантиметрах:")


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await UserState.weight.set()
    await message.answer("Введите ваш вес в килограммах:")


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    age = int(data["age"])
    growth = int(data["growth"])
    weight = int(data["weight"])

    bmr = 10 * weight + 6.25 * growth - 5 * age + 5
    await message.reply(f"Ваша норма калорий: {bmr} ккал в день.")

    await state.finish()


# Не по заданию , но хотелось очень добавить чтобы бот показал что вводить сперва
@dp.message_handler()
async def all_messages(message):
    await message.answer("Привет! Я посчитаю норму ваших каллорий в день. Введите 'Расчитать' чтобы начать.",
        reply_markup=kb)


if __name__=="__main__":
    executor.start_polling(dp, skip_updates=True)
