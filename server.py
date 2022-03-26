import logging

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = 'token'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    Функція для обробки команд
    """
    await message.reply("Привіт!\nОбери кімнату\n/room1\n/room2\n/room3\nа поки ця фішка не працює введіть слово кіт англійською в різних варіаціях")

@dp.message_handler(regexp='(^cat[s]?$|puss)')
async def cats(message: types.Message):
    with open('data/kit.jpg', 'rb') as photo:
        '''
        Функція відправляє фото з папки data 
        якщо отримує текстове повідомлення 
        зі словом cat
        '''

        await message.reply_photo(photo, caption='Cats are here 😺')

@dp.message_handler(regexp='(^Diana?$|puss)')
async def pdf_message(message: types.Message):
    with open('data/diana.jpeg', 'rb') as data:
        '''
        Функція відправляє файл презинтаії з папки data 
        якщо отримує текстове повідомлення 
        зі словом 
        '''

        await message.reply_photo(data, caption='Presentation especially for you ')



@dp.message_handler()
async def echo(message: types.Message): #ехо функція
    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
