from asyncio import run
from logging import basicConfig, INFO
from os import getenv
from dotenv import load_dotenv

from aiogram import Dispatcher, Bot
from aiogram.types import BotCommandScopeAllPrivateChats
from aiogram.client.bot import DefaultBotProperties
from aiogram.enums import ParseMode

from handlers.user_private import user_private_router
from cmd_list import private


async def main() -> None:
    load_dotenv()
    bot = Bot(getenv('bot_key'), default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    dp = Dispatcher()
    dp.include_router(user_private_router)

    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_my_commands(commands=private, scope=BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot)


if __name__ == "__main__":
    basicConfig(level=INFO)
    try:
        run(main())
    except KeyboardInterrupt:
        print('Exit')
