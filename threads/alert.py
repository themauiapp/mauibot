from client import get as get_client
from graphql_operations.expense import DAILYEXPENSES
from datetime import datetime
import threading


class Alert(threading.Thread):
    def __init__(self, name, chat_id, context, data):
        threading.Thread.__init__(self)
        self.name = name
        self.chat_id = chat_id
        self.context = context
        self.data = data

    def run(self):
        client = get_client(self.chat_id)
        now = datetime.now().strftime("%Y-%m-%d")
        query_params = {"date": now, "all": True}
        response = client.execute(DAILYEXPENSES, variable_values=query_params)
        expenses = response["dailyExpenses"]["expenses"]
        expenses_sum = response["dailyExpenses"]["sum"]
        self.notify(expenses, expenses_sum)

    def notify(self, expenses, expenses_sum):
        name = self.data["name"].split(" ")[0]
        currency = self.data["currency"]
        text = ""
        if len(expenses) == 0:
            text = "Hello {0}. Any expenses I should know about ?, I cannot find any expenses for you today".format(
                name
            )
            return self.context.bot.send_message(chat_id=self.chat_id, text=text)

        text = "You have spent {0} today. Here is the breakdown.\n".format(
            currency + "{:,}".format(expenses_sum)
        )
        for expense in expenses:
            name = expense["name"]
            amount = currency + "{:,}".format(expense["amount"])
            text = text + "{0} - {1}\n".format(name, amount)

        text = text + "Don't forget to record any extra expenses you incur."
        return self.context.bot.send_message(chat_id=self.chat_id, text=text)
