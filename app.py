from telegram.ext import (
    Updater,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    Filters,
)
from command_handlers.start import start_handler
from command_handlers.login import login_handler
from command_handlers.month import month_handler
from command_handlers.logout import logout_handler
from command_handlers.add import add_handler
from command_handlers.view import view_handler
from command_handlers.view_complete import view_complete_handler
from command_handlers.today import today_handler
from command_handlers.summary import summary_handler
from message_handlers.message import message_handler
from middlewares.auth import authenticated, guest
from jobs.send_alerts import send_alerts
from utilities.time import seconds_from_start
import datetime
import logging
import config
import pytz
import os

# Enable logging of errors
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

# Setting all relevant app configurations
config.set()

updater = Updater(token=config.get("bot_token"), use_context=True)
dispatcher = updater.dispatcher
job = updater.job_queue


def start(update, context):
    start_handler(update, context)


@guest
def login(update, context):
    login_handler(update, context)


@authenticated
def month(update, context):
    month_handler(update, context)


@authenticated
def add(update, context):
    add_handler(update, context)


@authenticated
def view(update, context):
    view_handler(update, context)


@authenticated
def view_complete(update, context):
    view_complete_handler(update, context)


@authenticated
def today(update, context):
    today_handler(update, context)


@authenticated
def summary(update, context):
    summary_handler(update, context)


@authenticated
def logout(update, context):
    logout_handler(update, context)


def message(update, context):
    message_handler(update, context)

# Setting all the jobs to alert users
job.run_repeating(send_alerts, interval=3600, first=seconds_from_start())

start_command_handler = CommandHandler("start", start)
login_command_handler = CommandHandler("login", login)
this_month_command_handler = CommandHandler("thismonth", month)
add_command_handler = CommandHandler("add", add)
view_command_handler = CommandHandler("view", view)
view_complete_command_handler = CallbackQueryHandler(view_complete)
today_command_handler = CommandHandler("today", today)
summary_command_handler = CommandHandler("summary", summary)
logout_command_handler = CommandHandler("logout", logout)
message_command_handler = MessageHandler(Filters.text, message)

dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(login_command_handler)
dispatcher.add_handler(this_month_command_handler)
dispatcher.add_handler(add_command_handler)
dispatcher.add_handler(view_command_handler)
dispatcher.add_handler(view_complete_command_handler)
dispatcher.add_handler(today_command_handler)
dispatcher.add_handler(summary_command_handler)
dispatcher.add_handler(logout_command_handler)
dispatcher.add_handler(message_command_handler)

updater.start_webhook(listen=config.get("bot_host"), port=config.get("bot_port"), url_path=config.get("bot_token"))
updater.bot.set_webhook(url="{0}{1}".format(config.get("bot_url"), config.get("bot_token")))

updater.idle()
