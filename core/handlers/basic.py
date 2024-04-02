from aiogram import Bot
from aiogram.types import Message
import json
from core.keyboards.reply import reply_keyboard, loc_tel_poll_keyboard, get_reply_keyboard

async def get_start(message: Message, bot: Bot):
    await message.answer(f'<s>Хех {message.from_user.first_name}!</s>',
                         reply_markup=get_reply_keyboard())

async  def get_location(message: Message, bot: Bot):
    await message.answer(f'Ты отправил локацию!\r\a'
                         f'{message.location.latitude}\r\n{message.location.longitude}')


async def get_photo(message: Message, bot: Bot):
    await message.answer(f'Бип.. Бап... Спасибо за ожидание!')
    file = await bot.get_file(message.photo[-1].file_id)
    await bot.download_file(file.file_path, f'photo.jpg')
    #await bot.download_file(file.file_path, f'{message.date.date()}{message.from_user.first_name}.jpg')


async def get_hello(message: Message, bot: Bot):
    await message.answer(f'И тебе привет!')
    json_str = json.dumps(message.dict(),default=str)
    print(json_str)