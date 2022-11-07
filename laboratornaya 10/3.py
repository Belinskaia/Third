from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from icrawler.builtin import GoogleImageCrawler

secret_token = '5635797798:AAHu8ZwtUpR-4GcKbjwadOJwmC3IsQOvPBE'

bot = Bot(token=secret_token)
dp = Dispatcher(bot)

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
    else:
        await bot.send_message(message.from_user.id, "https://www.google.com/search?q="+str(msg)+'&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjnxoCVxZz7AhXjlosKHUSzAZAQ_AUoAXoECAIQAw&biw=1920&bih=889&dpr=1')

if __name__ == '__main__':
    executor.start_polling(dp)
