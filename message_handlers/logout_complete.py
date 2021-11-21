from client import get as get_client
from graphql_operations.auth import LOGOUT
from utilities.actions import record as record_action
from utilities.tokens import delete as delete_token
from utilities.error_handler import handle_error
from utilities.users import delete as delete_user
import sys


def logout_complete(update, context):
    chat_id = str(update.effective_chat.id)
    message = update.message.text

    if message != "y" and message != "n":
        text = "Hmmm. I'm sorry, I do not understand that."
        return context.bot.send_message(chat_id=chat_id, text=text)


    if message == "n":
        text = "Ahhh nice. I'm happy you are not leaving me."
        record_action(chat_id, "logout_complete")
        return context.bot.send_message(chat_id=chat_id, text=text)

    try:
        client = get_client(chat_id)
        client.execute(LOGOUT)
        delete_token(chat_id)
        delete_user(chat_id)
        text = "Aye Aye. I have logged you out on here. Do return though. I enjoy your company."
        context.bot.send_message(chat_id=chat_id, text=text)
    except Exception:
        exception = sys.exc_info()
        return handle_error(chat_id, context, exception)
