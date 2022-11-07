from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from google_images_search import GoogleImagesSearch

from config import TOKEN

GCS_DEVELOPER_KEY= 'AIzaSyDbZ0bGtB7NvbGxZRINAXZ5eDuOE4pwcUQ'
GCS_CX = 'aef786076adc9270f'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
gis = GoogleImagesSearch(GCS_DEVELOPER_KEY, GCS_CX)


_search_params = {
    'q': '...',
    'num': 10,
    'safe': 'off',
    'fileType': 'jpg',
    'imgType': 'photo',
    'imgSize': 'MEDIUM',
    'imgDominantColor': 'pink',
    'imgColorType': 'color',
    'rights': 'cc_publicdomain'
}

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Hi! Wanna chat?")

@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("No help here")

@dp.message_handler(commands=['pic'])
async def photo(message: types.Message):
	msg = message.text[5:]
	if len(msg)==0:
		await bot.send_message(message.from_user.id, "no input")
	else: await message.answer_photo('https://www.google.com/search?q='+msg+'&tbm=isch')

@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text) 

if __name__ == '__main__':
    executor.start_polling(dp)
