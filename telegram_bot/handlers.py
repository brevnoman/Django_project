from telegram.ext import CommandHandler
from telegram_bot.controller import say_me_when


say_me_when_hendler = CommandHandler("say_me_when", say_me_when)