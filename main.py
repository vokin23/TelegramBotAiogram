import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import BotCommandScopeAllPrivateChats

from config import TOKEN
from common.bot_comand_list import private
from handlers.user_private import user_private_router

ALLOWED_UPDATES = ['message, edited_message']

bot = Bot(token=TOKEN)
dp = Dispatcher()
dp.include_routers(user_private_router)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_my_commands(commands=private, scope=BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)


if __name__ == '__main__':
    asyncio.run(main())
