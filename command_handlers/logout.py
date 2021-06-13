from utilities.actions import record as record_action

def logout_handler(update, context):
    chat_id = str(update.effective_chat.id)
    text = "Are you 100% sure you want to logout? Reply y for yes or n for no."
    record_action(chat_id, 'logout')
    context.bot.send_message(chat_id=chat_id, text=text)