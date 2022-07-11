
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.utils.markdown import hbold,hlink
from main import collect_data, return_back
import json
import time



bot = Bot(token='5559972344:AAEDQXAYPlyBCB94EpMKSnbxef_9pvfV138',parse_mode=types.ParseMode.HTML )
dp = Dispatcher(bot)



@dp.message_handler(commands='start')
async def start(message:types.Message):
    start_btn = ['Ножи','Перчатки']
    next_btn = ['Вернуться назад']
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_btn)
    keyboard.add(*next_btn)

    await message.answer('Выберите категорию', reply_markup=keyboard)


    



@dp.message_handler(Text(equals='Ножи'))
async def get_discount_knives(message:types.Message):
    await message.answer('Пожалуйста подождите...')

    collect_data(type_card=2)
        


    with open(f'result.json', encoding='utf-8') as file:

        data = json.load(file)


    for index,item in enumerate(data):
        card = f'{hlink(item.get("full_name"),item.get("3d"))}\n' \
            f'{hbold("Скидка: ")}{item.get("overprice")}%\n' \
            f'{hbold("Цена: ")}${item.get("item_price")}\n'

        if index%20 == 0:
            time.sleep(3)

        await message.answer(card)

@dp.message_handler(Text(equals='Перчатки'))
async def get_discount_knives(message:types.Message):
    await message.answer('Пожалуйста подождите...')

    collect_data(type_card=13)
        


    with open(f'result.json', encoding='utf-8') as file:

        data = json.load(file)


    for index,item in enumerate(data):
        card = f'{hlink(item.get("full_name"),item.get("3d"))}\n' \
            f'{hbold("Скидка: ")}{item.get("overprice")}%\n' \
            f'{hbold("Цена: ")}${item.get("item_price")}\n'

        if index%20 == 0:
            time.sleep(3)

        await message.answer(card)

@dp.message_handler(Text(equals='Вернуться назад'))
async def back_to_start(message:types.Message):
    await message.answer('Возвращаю обратно...')
    time.sleep(3)
    await message.answer('Выберите категорию')

    return_back()
    

def main():
    executor.start_polling(dp)

if __name__ == '__main__':
    main()