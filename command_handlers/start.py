import config
import os

def start_handler(update, context):
    chat_id = str(update.effective_chat.id)
    app_root = config.get('app_root')
    with open(os.path.join(app_root, 'messages', 'start.txt'), 'r') as reader:
        text = reader.read()
    
    context.bot.send_message(chat_id=chat_id, text=text)