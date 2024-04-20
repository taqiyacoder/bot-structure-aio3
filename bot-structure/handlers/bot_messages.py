from aiogram import Router, F
from aiogram.types import Message 
from aiogram.filters import Command, CommandStart


router = Router()


@router.message(CommandStart())
async def start_handler(message: Message) -> None:
    await message.answer(
        f"Hello world",
    )