from utilities.actions import record as record_action


def add_handler(update, context):
    chat_id = str(update.effective_chat.id)
    text = "Alrighty. What is the name of the expense?"
    record_action(chat_id, "add")
    return context.bot.send_message(chat_id=chat_id, text=text)
