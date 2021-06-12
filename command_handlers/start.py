from telegram import ParseMode
import config
import random
import os

def start_handler(update, context):
    chat_id = str(update.effective_chat.id)
    app_root = config.get('app_root')
    greetings = ['Hey there.', 'Hello.', 'Hi.', 'Heyaa.']
    greeting = greetings[random.randint(0, len(greetings) - 1)]
    with open(os.path.join(app_root, 'messages', 'start.txt'), 'r') as reader:
        text = reader.read().format(greeting)
    
    context.bot.send_message(chat_id=chat_id, text=text, parse_mode=ParseMode.HTML)