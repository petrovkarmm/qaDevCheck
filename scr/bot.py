import asyncio
from turtledemo.clock import setup

from aiogram import Dispatcher, Bot, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.base import DefaultKeyBuilder
from aiogram.fsm.storage.redis import RedisStorage
from aiogram.types import Message
from aiogram_dialog import setup_dialogs

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

    @dp.message(F.text)
    async def test_handler(message: Message, state: FSMContext):
        await message.answer(
            text=message.text
        )

    setup_dialogs(dp)

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
