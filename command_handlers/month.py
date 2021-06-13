from telegram import ChatAction
from datetime import datetime
from client import get as get_client
from graphql_operations.income import CURRENTMONTHINCOME
from utilities.actions import record as record_action
from utilities.users import get as get_users
import config
import os.path as path

def month_handler(update, context):
    chat_id = str(update.effective_chat.id)
    context.bot.send_chat_action(chat_id=chat_id, action=ChatAction.TYPING)
    client = get_client(chat_id)
    response = client.execute(CURRENTMONTHINCOME)
    data = response['currentMonthIncome']
    record_action(chat_id, 'thismonth')

    if data is None:
        text = 'Hmmm. I cannot find any income information belonging to you for this month.'
        return context.bot.send_message(chat_id=chat_id, text=text)

    currency = get_users().get(chat_id)['currency']
    dateText = datetime.now().strftime("%B %Y")
    data['spent'] = data['total'] - data['remainder']
    data['percent_spent'] = round((data['spent'] / data['total']) * 100, 2)
    data['percent_spent'] = str(data['percent_spent']) + '%'
    text = get_month_text().format(dateText,
    currency + "{:,}".format(data['total']),
    currency + "{:,}".format(data['spent']),
    data['percent_spent'],
    currency + "{:,}".format(data['remainder']),
    data['percent_remainder'],
    data['expenses_count'])

    context.bot.send_message(chat_id=chat_id, text=text)

def get_month_text():
    app_root = config.get('app_root')
    with open(path.join(app_root, 'messages', 'this_month.txt'), 'r') as reader:
        text = reader.read()
    return text