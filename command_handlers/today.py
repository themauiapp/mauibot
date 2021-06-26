from telegram import ChatAction
from command_handlers.view_complete import fetch_expenses, parse_text
from utilities.actions import record as record_action
from datetime import datetime

def today_handler(update, context):
    chat_id = str(update.effective_chat.id)
    context.bot.send_chat_action(chat_id=chat_id, action=ChatAction.TYPING)
    now = datetime.now()
    formatted_date = now.strftime("%Y-%m-%d")
    response = fetch_expenses(chat_id, formatted_date)
    data = response['dailyExpenses'];
    text = parse_text(chat_id, data, now, True)
    record_action(chat_id, 'today')
    context.bot.send_message(chat_id=chat_id, text=text)

