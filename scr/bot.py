import asyncio

from aiogram import Dispatcher, Bot
from aiogram.fsm.storage.base import DefaultKeyBuilder
from aiogram.fsm.storage.redis import RedisStorage
from aiogram_dialog import setup_dialogs

from scr.dialogs.qa_menu_dialog_router import qa_menu_dialog_router
from scr.routers.start.start_router import start_router
from scr.settings import DEBUG, redis_connect_url, bot_test_token, bot_token


async def bot_start():
    if DEBUG:
        dp = Dispatcher()
        bot = Bot(token=bot_test_token)
    else:

        storage = RedisStorage.from_url(
            redis_connect_url, key_builder=DefaultKeyBuilder(with_destiny=True)
        )
        dp = Dispatcher(storage=storage)
        bot = Bot(token=bot_token)

    setup_dialogs(dp)

    dp.include_router(
        start_router
    )

    dp.include_router(
        qa_menu_dialog_router
    )

    await bot.delete_webhook(
        drop_pending_updates=True
    )

    await dp.start_polling(
        bot
    )


if __name__ == "__main__":
    try:
        asyncio.run(
            bot_start()
        )

        print('Bot start.')

    except Exception as e:
        print(e)
