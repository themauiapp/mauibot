from utilities.users import get as get_users
from client import get as get_client
from graphql_operations.user import FETCHUSERSTONOTIFY
from datetime import datetime
from threads.alert import Alert
import pytz


def send_alerts(context):
    if not determine_valid_time():
        return

    users = fetch_users()

    for chat_id, data in users:
        name = "thread-{0}".format(chat_id)
        alert = Alert(name, chat_id, context, data)
        alert.run()

def fetch_users():
    time = datetime.now((pytz.timezone('Africa/Lagos'))).strftime("%I%p").lower()
    time = time[1:] if time[0] == '0' else time
    client = get_client()
    variables = {"time": time}
    response = client.execute(FETCHUSERSTONOTIFY, variable_values=variables)
    user_chat_ids = list(map(lambda user: user['telegram']['telegram_id'], response['usersByTelegramSetting']))
    users = list(filter(lambda user: user[0] in user_chat_ids , get_users().items()))
    print(users)
    return users

def determine_valid_time():
    hour = int(datetime.now((pytz.timezone('Africa/Lagos'))).strftime("%H"))
    return hour == 12 or hour == 18 or hour == 22
