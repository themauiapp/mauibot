from telegram import ChatAction
from utilities.actions import record as record_action
from utilities.users import get as get_users
from graphql_operations.income import INCOMESTATS
from client import get as get_client


def summary_handler(update, context):
    chat_id = str(update.effective_chat.id)
    context.bot.send_chat_action(chat_id=chat_id, action=ChatAction.TYPING)
    client = get_client(chat_id)
    try:
        response = client.execute(INCOMESTATS)
    except Exception:
        return ""
    data = response["incomeStats"]
    currency = get_users()[chat_id]["currency"]
    income_data = {
        "Total Income Earned": currency + "{:,}".format(data["income_total"]),
        "Income Spent": currency + "{:,}".format(data["income_spent"]),
        "Income Remaining": currency + "{:,}".format(data["income_remainder"]),
    }
    text = "Here are your income statistics since you started using Maui.\n"

    for key, value in income_data.items():
        text += "{0} - {1}\n".format(key, value)

    record_action(chat_id, "summary")
    context.bot.send_message(chat_id=chat_id, text=text)
