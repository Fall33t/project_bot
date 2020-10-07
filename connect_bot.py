import logging
import cbot_settings
from telegram.ext import Updater, CommandHandler
logging.basicConfig(filename='cbot.log', level=logging.INFO)
def tcp(update, context):
    update.message.reply_text('TCP!')


def greet_user(update, context):
    update.message.reply_text('Привет пользователь! Доступные команды бота: /TCP')
def main():
    connect_bot = Updater(cbot_settings.API_KEY , use_context=True)
    dp = connect_bot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("TCP", tcp))
    connect_bot.start_polling()
    connect_bot.idle()
if __name__ == '__main__':
    main()    