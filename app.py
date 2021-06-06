from telegram.ext import Updater, CommandHandler
from command_handlers.start import start_handler
import logging
import config

# Enable logging of errors
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Setting all relevant app configurations
config.set()

updater = Updater(token=config.get("bot_token"), use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
    start_handler(update, context)

start_command_handler = CommandHandler('start', start)

dispatcher.add_handler(start_command_handler)

updater.start_polling()
updater.idle()