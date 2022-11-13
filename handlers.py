# Здесь хранятся хендлеры

from aiogram import Dispatcher

import commands


def registred_handlers(dp: Dispatcher):
    dp.register_message_handler(commands.start, commands=['start'])
    dp.register_message_handler(commands.get_first_player, commands=['choice'])
    dp.register_message_handler(commands.finish, commands=['finish'])
    dp.register_message_handler(commands.getNumber)