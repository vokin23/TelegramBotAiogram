from aiogram import types, Router
from aiogram.filters import CommandStart, Command
from filters.chat_types import ChatTypeFilter

from kbds import reply


user_private_router = Router()
user_private_router.message.filter(ChatTypeFilter(['private']))


@user_private_router.message(CommandStart())
async def start(message: types.Message):
    await message.answer('Start!', reply_markup=reply.start_kb)


@user_private_router.message(Command('help'))
async def helps(message: types.Message):
    await message.answer('help!')


@user_private_router.message(Command('about'))
async def about(message: types.Message):
    await message.answer('about!')
