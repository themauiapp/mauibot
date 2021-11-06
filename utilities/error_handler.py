from utilities.users import get as get_users


def handle_error(chat_id, error_id, context):
    error_text = "I'm sorry. I encountered an error carrying out that operation. Try again later and I should have it all sorted out."
    if error_id == "AuthenticationFailed":
        error_text = (
            "Hmmm. I cannot find a Maui user with the email and password you entered."
        )

    if error_id == "AuthenticatedToTelegramAlready":
        error_text = "You are logged in already on a different Telegram account."

    return context.bot.send_message(chat_id=chat_id, text=error_text)
