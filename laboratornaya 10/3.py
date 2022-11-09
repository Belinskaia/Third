from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

secret_token = '5635797798:AAHu8ZwtUpR-4GcKbjwadOJwmC3IsQOvPBE'
bot = Bot(token=secret_token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['Salute'])
async def process_start_command(message: types.Message):
    await message.reply('Hello, I wait for a request of the form: out main_word')

@dp.message_handler(commands=['out'])
async def photo(message: types.Message):
    msg = message.text[5:]
    img = 'https://htstatic.imgsmail.ru/pic_image/0efda7a7a24673153e86521d430076e3/840/526/2269298/'
    import urllib
    photo = urllib.urlretrieve(img, "...\img.jpg") 
    await bot.send_photo(message.from_user.id, photo)

if __name__ == '__main__':
    executor.start_polling(dp)
