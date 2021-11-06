from utilities.users import get as get_users
from threads.alert import Alert

def send_alerts(context):
    users = get_users()
    
    for chat_id, data in users.items():
        name = 'thread-{0}'.format(chat_id)
        alert = Alert(name, chat_id, context, data)
        alert.run()
