# Здесь что-то типа контроллера связывающий хендлеры и вью

from aiogram import types

import model
import view
from bot import bot
from random import randint


candies_count = model.total_count
digit = 0 

async def start(message: types.Message):   
    await view.greetings(message)


async def get_first_player(message: types.Message):  # Выбираем случайную очередность
    rand_digit = randint(0, 1)
    await view.priority(rand_digit, message)
    await start_game(message, rand_digit, model.total_count)

async def start_game(message, my_digit, total_count):
    global candies_count
    global digit
    global count
    candies_count = total_count
    digit = my_digit    
    if digit == 0:
        await Get_numbers_of_candies(message)
    else:        
        count = await move_of_bot(message, candies_count)
        candies_count = count       
        await Get_numbers_of_candies(message)

async def continue_game(message: types.Message, my_candies_count, my_digit):
    global digit
    global count
    global candies_count
    digit=my_digit    
    candies_count = my_candies_count    
    await view.remains_candies_on_the_table(message, candies_count)
    if candies_count > 28:
        if digit == 1:
            digit = 0
            await Get_numbers_of_candies(message)        
        else:
            count = await move_of_bot(message, candies_count)
            candies_count = count            
            await Get_numbers_of_candies(message)
    else:
        if digit == 0 and candies_count !=0:
            await view.win_bot(message, candies_count)            
        else:
            await view.win_human(message, candies_count)
            
        
       

async def move_of_bot(message: types.Message, count_candies):
    
    global digit
    global candies_count
    candies_count = count_candies  
    k = await Get_numbers_of_candies_from_bot(message, candies_count)    
    candies_count -= k    
    digit = 0    
    await view.remains_candies_on_the_table(message, candies_count)
    return candies_count


async def Get_numbers_of_candies(message: types.Message):
    global candies_count
    global digit    
    await view.question_move_of_player(message) 



async def Get_numbers_of_candies_from_bot(message, col):
    if col > 80:
       col = randint(1, 28) 
    else:
        col = col%29
        if col == 0:
            col = randint(1, 28)
    await view.move_of_bot(message, col)
    return (col)
   


async def finish(message: types.Message):
    await bot.send_message(message.from_user.id,
                        f'{message.from_user.first_name}, '
                        f'до свидания!')


async def getNumber(message: types.Message):
    global number
    global candies_count
    global digit    
    number = message.text
    if int(number) < 1 or int(number) > 28:
        await view.error_of_numbers(message)
    else:
        number=int(number)        
        candies_count -= number             
        await continue_game(message, candies_count, digit)

