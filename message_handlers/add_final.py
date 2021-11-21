from utilities.actions import record as record_action
from utilities.expenses import get as get_expenses
from utilities.users import get as get_users
from utilities.error_handler import handle_error
from graphql_operations.expense import ADDEXPENSE
from client import get as get_client


def add_final(update, context):
    chat_id = str(update.effective_chat.id)
    amount = update.message.text

    if amount.isnumeric() is False:
        text = "Please enter a valid amount."
        return context.bot.send_message(chat_id=chat_id, text=text)

    expense = get_expenses()[chat_id]
    params = {"name": expense, "amount": float(amount)}
    client = get_client(chat_id)
    response = client.execute(ADDEXPENSE, variable_values=params)
    data = response["addExpense"]
    print("My name is Olamileke")

    if data["errorId"]:
        return handle_error(chat_id, data["errorId"], context)

    currency = get_users()[chat_id]["currency"]
    print(data)
    total = currency + "{:,}".format(data["sum"])
    text = "Okay. I have recorded {0} successfully. That brings your total spent today to {1}.".format(
        expense, total
    )
    record_action(chat_id, "add_final")
    context.bot.send_message(chat_id=chat_id, text=text)
