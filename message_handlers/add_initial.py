from utilities.actions import record
from utilities.actions import record as record_action
from utilities.expenses import record as record_expense


def add_initial(update, context):
    chat_id = str(update.effective_chat.id)
    expense = update.message.text.lower()
    record_expense(chat_id, expense)
    record_action(chat_id, "add_initial")
    text = "And how much did you spend on {0}?".format(update.message.text)
    context.bot.send_message(chat_id=chat_id, text=text)
