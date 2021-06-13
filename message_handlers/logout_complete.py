from client import get as get_client
from graphql_operations.auth import LOGOUT
from utilities.actions import record as record_action
from utilities.tokens import delete as delete_token
from utilities.users import delete as delete_user

def logout_complete(update, context):
    chat_id = str(update.effective_chat.id)
    message = update.message.text

    if message != 'y' and message != 'n':
        text = "Hmmm. I'm sorry, I do not understand that."
        return context.bot.send_message(chat_id=chat_id, text=text)

    record_action(chat_id, 'logout_complete')

    if message == 'n':
        text = "Ahhh nice. I'm happy you are not leaving me."
        return context.bot.send_message(chat_id=chat_id, text=text)

    client = get_client(chat_id)
    client.execute(LOGOUT)
    delete_token(chat_id)
    delete_user(chat_id)
    text = 'Aye Aye. I have logged you out on here. Do return though. I enjoy your company.'
    context.bot.send_message(chat_id=chat_id, text=text)



    

    