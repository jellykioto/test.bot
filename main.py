from aiogram import Bot, Dispatcher, F
from core.handlers.basic import get_start, get_photo, get_hello
from core.handlers.contact import get_fake_contact, get_true_contact
from core.filters.iscontact import IsTrueContact
import asyncio
import logging
from core.settings import settings
from aiogram.filters import Command
from core.utils.commands import set_commands
from core.handlers.basic import get_location


async def start_bot(bot: Bot):
    await set_commands(bot)
    await bot.send_message(settings.bots.admon_id, text='Бот запущен')

async def stop_bot(bot: Bot):
    await bot.send_message(settings.bots.admon_id, text='Бот остановлен')




 # log level
logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s - [%(levelname)s] - %(name)s - "
                           "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
                    )

# bot init
async def start():
    bot = Bot(token=settings.bots.bot_token, parse_mode='HTML')

    dp = Dispatcher()
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
    dp.message.register(get_location, F.location)
    dp.message.register(get_hello, F.text.lower() == 'привет')
    dp.message.register(get_true_contact, F.contact, IsTrueContact())
    dp.message.register(get_fake_contact, F.contact)
    dp.message.register(get_photo, F.photo)
    dp.message.register(get_start, Command(commands=['start', 'run']))

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(start())
