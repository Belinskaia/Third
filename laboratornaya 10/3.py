from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import requests
from bs4 import BeautifulSoup
import lxml

bot = Bot(token='5635797798:AAHu8ZwtUpR-4GcKbjwadOJwmC3IsQOvPBE')
dp = Dispatcher(bot)

@dp.message_handler(commands=['Hello'])
async def process_start_command(message: types.Message):
    await message.reply("Salute! You can get picture)")

@dp.message_handler()
async def photo(message: types.Message):
    URL = 'https://images.search.yahoo.com/search/images;_ylt=AwrEqMqhMWljIE40j31XNyoA;_ylu=Y29sbwNiZjEEcG9zAzEEdnRpZANMT0NVSTA1M18xBHNlYwNwaXZz?p='+message.text[3:]+'&fr2=piv-web&fr=yfp-t'
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, 'lxml')
    q = soup.select('img[src]')
    await bot.send_photo(message.from_user.id, q[0]['src'])

if __name__ == '__main__':
    executor.start_polling(dp)
