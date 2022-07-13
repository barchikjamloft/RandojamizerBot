import logging
import os

from aiogram import Bot, Dispatcher, executor, types

from .randojam import Randojam

API_TOKEN = os.getenv('API_TOKEN')

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN, parse_mode='html')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """

    await message.reply("Hi! Use /randojamize command to have some fun with your musical folks ")


@dp.message_handler(commands=['randojamize'])
async def send_randojamize(message: types.Message):
    """
    `/randojamize` command
    """

    jam = Randojam()

    text = [
        "<b>It's jam time 😎</b>\n",
        f'Genre: {jam.genre}',
        f'Time signature: {jam.time}',
        f'Tempo: {jam.tempo}',
        f'Tonality: {jam.tonality}',
        f'Progression: {jam.progression}',
        '\n<i>Have fun!</i>']

    await message.answer('\n'.join(text))


def run():
    executor.start_polling(dp, skip_updates=True)
