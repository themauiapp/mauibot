from client import get as get_client
from graphql_operations.auth import LOGIN
from utilities.actions import record as record_action
from utilities.tokens import record as record_token
from utilities.users import record as record_user
from utilities.error_handler import handle_error
import re

def login_complete(update, context):
    chat_id = str(update.effective_chat.id)
    message = update.message.text
    credentials = message.split(' ')

    if len(credentials) != 2:
        text = 'I only need your Maui email and password. No more, No less.'
        return context.bot.send_message(chat_id=chat_id, text=text) 

    email,password = credentials
    email_regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

    if re.match(email_regex, email) is None:
        text = 'I need a valid email address'
        return context.bot.send_message(chat_id=chat_id, text=text)

    if len(password) < 8:
        text = 'That is definitely not your Maui password. Maui passwords are at least 8 characters in length.'
        return context.bot.send_message(chat_id=chat_id, text=text)  

    client = get_client(chat_id)
    query_params = { 'email':email, 'password':password }
    response = client.execute(LOGIN, variable_values=query_params)
    data = response['statelessLogin']

    if data['errorId'] is not None: 
        return handle_error(chat_id, data['errorId'], context)

    token = data['token']
    record_token(chat_id, token)
    record_action(chat_id, 'login_complete')
    record_user(chat_id, data['user'])
    
    name = data['user']['name'].split(' ')[1]
    text = "Hello {0}. Really nice to meet you. I trust we will have a fun time together. I'm ready and at your service.".format(name)
    context.bot.send_message(chat_id=chat_id, text=text)