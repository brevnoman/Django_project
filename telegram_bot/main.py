from telegram.ext import Updater
from telegram_bot.utils import get_logger
from telegram_bot.handlers import say_me_when_hendler
from telegram_bot.models import Base, engine


def main():
    my_token = open("token.txt").read()
    updater = Updater(token=my_token, use_context=True)
    get_logger()
    dp = updater.dispatcher
    updater.start_polling()
    dp.add_handler(say_me_when_hendler)
    updater.idle()


if __name__ == '__main__':
    Base.metadata.create_all(engine)

    main()