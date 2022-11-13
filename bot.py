#Здесь создается бот 
import model
from aiogram import Bot
from aiogram.dispatcher import Dispatcher


bot = Bot(model.token)
dp = Dispatcher(bot)