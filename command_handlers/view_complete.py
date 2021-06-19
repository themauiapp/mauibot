from telegram import ChatAction, ReplyKeyboardRemove
from utilities.actions import record as record_action
from utilities.users import get as get_users
from client import get as get_client
from graphql_operations.expense import DAILYEXPENSES
import packages.calendar as calendar

def view_complete_handler(update, context):
    chat_id = str(update.callback_query.from_user.id)
    selected,date = calendar.process_calendar_selection(context.bot, update)

    if not selected:
        return
    
    context.bot.send_chat_action(chat_id=chat_id, action=ChatAction.TYPING)
    formatted_date = date.strftime("%Y-%m-%d")
    response = fetch_expenses(chat_id, formatted_date)
    data = response['dailyExpenses'];
    text = parse_text(chat_id, data, date)
    record_action(chat_id, 'view_complete')
    context.bot.send_message(chat_id=chat_id, text=text, reply_markup=ReplyKeyboardRemove())

def fetch_expenses(chat_id, date):
    client = get_client(chat_id)
    query_params = {"date": date, "all": True}
    return client.execute(DAILYEXPENSES, variable_values=query_params)

def parse_text(chat_id, data, date):
    day = date.strftime("%d")
    parsed_date = date.strftime("%A, {0} %B %Y").format(get_suffixed_day(int(day)))

    if data['sum'] == 0:
        text = 'I cannot find any expenses for {0}'.format(parsed_date)
        return text

    currency = get_users()[chat_id]['currency']
    expenses_sum = currency +  "{:,}".format(data['sum'])
    text = 'On {0} you spent {1}\n'.format(parsed_date, expenses_sum)
    for expense in data['expenses']:
        name = expense['name']
        amount = currency + "{:,}".format(expense['amount'])
        text = text + '{0} - {1}\n'.format(name,amount)
    return text

def get_suffixed_day(day):
    return str(day) + 'th' if 11<=day<=13 else str(day) + {1: 'st', 2: 'nd', 3: 'rd'}.get(day%10, 'th')