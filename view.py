# Cюда все функции отправляющие сообщения

import model
from aiogram import types
from bot import bot


async def greetings(message: types.Message):
    await bot.send_message(message.from_user.id,
                           f'{message.from_user.first_name}, привет!\n'
                           f'Это игра в конфетки.\n'
                           f'Мы по очереди берем конфеты в любом количестве, но не больше 28.\n'
                           f'Выигрывает и забирает все конфеты тот, кто сделает последний ход.\n'
                           f'Для случайного выбора первого ходящего набери "/choice"\n'
                           f'Для выхода набери "/finish"')

async def priority(prior, message: types.Message):
    if prior == 0:
        await bot.send_message(message.from_user.id,
                           f'{message.from_user.first_name}, первым конфеты берешь ты.\n'
                           f'Всего на столе {model.total_count} конфет.')
    else:
        await bot.send_message(message.from_user.id,
                           f'Первым конфеты беру я.\n'
                           f'Всего на столе {model.total_count} конфет.')

async def move_of_bot(message: types.Message, col_candies):
    await bot.send_message(message.from_user.id,
                          f'Я беру {col_candies} конфет.')

async def remains_candies_on_the_table(message: types.Message, col_candies):
    await bot.send_message(message.from_user.id,
                            f'На столе осталось {col_candies} конфет.')

async def question_move_of_player(message: types.Message):
    await bot.send_message(message.from_user.id,
                            f'Cколько возьмешь конфет?\n')
  

async def error_of_numbers(message: types.Message):
    await bot.send_message(message.from_user.id,
                            f'Ты ввел неверное количество конфет!\n'
                            f'Попробуй еще раз:')

async def win_bot(message: types.Message, col_candies):
      await bot.send_message(message.from_user.id,
                            f'Я беру оставшиеся {col_candies} конфет и выигрываю. \n'
                            f'Все конфеты мои!\n'
                            f'Если хочешь еще сыграть - набери "/start".\n'
                            f'Чтобы закончить - набери "/finish".\n')

async def win_human(message: types.Message, col_candies):
                           await bot.send_message(message.from_user.id,
                           f'{message.from_user.first_name}, поздравляю, ты выиграл.\n'
                           f'Все конфеты твои!\n'
                           f'Если хочешь еще сыграть - набери "/start".\n'
                           f'Чтобы закончить - набери "/finish".\n')                                                

                          
