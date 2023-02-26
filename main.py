import logging
import json
from scraper import collect_video
from aiogram import Bot, Dispatcher, executor, types
from random import shuffle


API_TOKEN = ''

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Я могу прислать вам топ песен недели на ютуб! Просто введите команду /music-yt.\nВ будущем смогу присылать выборку фильмов!")


@dp.message_handler(commands=['music-yt', ])
async def send_top_movie(message: types.Message):
    collect_video()
    text = ''
    with open('data.json', 'r') as file:
        data = json.load(file)

    shuffle(data['content'])

    for i in data['content'][0:5]:
        if i is not None:
            text += f'[{i["name"]}]({i["url"]})\n'

    await message.reply(text, parse_mode=types.ParseMode.MARKDOWN, disable_web_page_preview=True)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
