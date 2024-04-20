import asyncio
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties

import logging

from config import TOKEN
from handlers import bot_messages, questionaire




async def main() -> None:
    #logging
    logging.basicConfig(level=logging.INFO)

    #dispatcher, bot
    bot = Bot(
        token=TOKEN,
        default=DefaultBotProperties(parse_mode='HTML')
    )
    dp = Dispatcher()

    #routers
    dp.include_routers(
        bot_messages.router,
        questionaire.router
    )

    #start
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)




if __name__ == "__main__":
    try:
        asyncio.run(main())
    except:
        print("\033[38;5;196mgoodbye\033[0m")