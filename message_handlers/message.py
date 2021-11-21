from telegram import ChatAction
from message_handlers.login_complete import login_complete
from message_handlers.add_initial import add_initial
from message_handlers.add_final import add_final
from message_handlers.logout_complete import logout_complete
from utilities.actions import get_latest as get_latest_action


def message_handler(update, context):
    chat_id = str(update.effective_chat.id)
    latest_action = get_latest_action(chat_id)
    context.bot.send_chat_action(chat_id=chat_id, action=ChatAction.TYPING)

    if latest_action == "login":
        return login_complete(update, context)

    if latest_action == "add":
        return add_initial(update, context)

    if latest_action == "add_initial":
        return add_final(update, context)

    if latest_action == "logout":
        return logout_complete(update, context)

    text = "Hmmm. I'm sorry. I don't understand that. Type /start to see a list of my commands."
    return context.bot.send_message(chat_id=chat_id, text=text)
