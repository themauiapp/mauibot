from utilities.users import get as get_users
import functools


def authenticated(handler):
    @functools.wraps(handler)
    def middleware(update, context):
        chat_id = str(update.effective_chat.id)
        users = get_users()

        if users.get(chat_id) is None:
            text = "I'm sorry. I do not know who you are. Login and I can process that command."
            return context.bot.send_message(chat_id=chat_id, text=text)

        return handler(update, context)

    return middleware


def guest(handler):
    @functools.wraps(handler)
    def middleware(update, context):
        chat_id = str(update.effective_chat.id)
        user = get_users().get(chat_id)

        if user is not None:
            name = user["name"].split(" ")[1]
            text = "I know who you are already {0}".format(name)
            return context.bot.send_message(chat_id=chat_id, text=text)

        return handler(update, context)

    return middleware
