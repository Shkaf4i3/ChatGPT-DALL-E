from aiogram.utils.keyboard import ReplyKeyboardBuilder


async def main_kb():
    keyboard = ReplyKeyboardBuilder()
    keyboard.button(text='Выполнить запрос 📊'),
    keyboard.button(text='Сгенерировать фото 🥝'),
    keyboard.button(text='О боте 🥝')
    return keyboard.adjust(2).as_markup(resize_keyboard=True)


async def back_main_kb():
    keyboard = ReplyKeyboardBuilder()
    keyboard.button(text='Вернуться в меню 👈')
    return keyboard.as_markup(resize_keyboard=True)


async def break_prompt_kb():
    keyboard = ReplyKeyboardBuilder()
    keyboard.button(text='Отменить запрос ❌')
    return keyboard.as_markup(resize_keyboard=True)
