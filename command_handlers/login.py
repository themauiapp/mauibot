from telegram import ParseMode
import config
import os.path as path
from utilities.actions import record as record_action

def login_handler(update, context):
    chat_id = str(update.effective_chat.id)
    app_root = config.get('app_root')
    with open(path.join(app_root, 'messages', 'login.txt'), 'r') as reader:
        text = reader.read()

    record_action(chat_id, 'login')
    context.bot.send_message(chat_id=chat_id, text=text, parse_mode=ParseMode.HTML)