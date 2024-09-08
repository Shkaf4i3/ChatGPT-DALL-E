from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

import reply as kb
from handlers.function import generate_answer, generate_image


user_private_router = Router()


class Generate_prompt(StatesGroup):
    prompt_answer = State()
    prompt_photo = State()


@user_private_router.message(CommandStart())
async def start_message(message: Message):
    await message.answer(f'Привет, {message.from_user.first_name} ❤️\n'
                        'Для продолжения работы воспользуйся меню',
                        reply_markup=await kb.main_kb())


@user_private_router.message(Command('help'))
async def help_message(message: Message):
    await message.answer('Любые вопросы по боту сюда 👉 @shkaf4i3')


@user_private_router.message(F.text == 'О боте 🥝')
async def about_info(message: Message):
    await message.answer('🪬 Данный бот - генеративный искусственный интеллект ChatGPT 4 🪬',
                        reply_markup=await kb.back_main_kb())


@user_private_router.message(F.text == 'Вернуться в меню 👈')
async def back_menu(message: Message):
    await message.answer('Вы вернулись в меню 💋', reply_markup=await kb.main_kb())


@user_private_router.message(F.text == 'Выполнить запрос 📊')
async def request_answer_message(message: Message, state: FSMContext):
    await state.set_state(Generate_prompt.prompt_answer)
    await message.answer('Введите запрос 👉', reply_markup=await kb.break_prompt_kb())


@user_private_router.message(Generate_prompt.prompt_answer)
async def get_answer_message(message: Message, state: FSMContext):
    await state.update_data(prompt_answer=message.text)
    user_text = message.text
    create_answer = await generate_answer(message.text)

    if user_text == 'Отменить запрос ❌':
        await message.answer('Вы вернулись в меню', reply_markup=await kb.main_kb())
    else:
        await message.answer(f'{create_answer}')
    await state.clear()


@user_private_router.message(F.text == 'Сгенерировать фото 🥝')
async def request_photo(message: Message, state: FSMContext):
    await state.set_state(Generate_prompt.prompt_photo)
    await message.answer('Введите запрос к фото 🪬', reply_markup=await kb.break_prompt_kb())


@user_private_router.message(Generate_prompt.prompt_photo)
async def get_photo(message: Message, state: FSMContext):
    await state.update_data(prompt_photo=message.text)
    user_text = message.text
    create_photo = await generate_image(message.text)

    if user_text == 'Отменить запрос ❌':
        await message.answer('Вы вернулись в меню', reply_markup=await kb.main_kb())
    else:
        await message.answer(f'{create_photo}')
    await state.clear()
