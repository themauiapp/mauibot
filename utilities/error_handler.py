from utilities.users import get as get_users
from utilities.logs import record as record_exception
import traceback

def handle_error(chat_id=None, context=None, exception=None, error_id=None):
    error_text = "I'm sorry. I encountered an error carrying out that operation. Try again later and I should have it all sorted out."

    if exception:
        parsed_exception = {
            "message": str(exception[1]),
            "type": str(exception[0]),
            "stack_trace": " ".join(traceback.format_exception(*exception)),
        }
        record_exception(parsed_exception)

    if error_id:
        error_text = get_error_text(error_id)

    if chat_id and context:
        return context.bot.send_message(chat_id=chat_id, text=error_text)

def get_error_text(error_id):
    error_text = "I'm sorry. I encountered an error carrying out that operation. Try again later and I should have it all sorted out."
    if error_id == "AuthenticationFailed":
        error_text = (
            "Hmmm. I cannot find a Maui user with the email and password you entered."
        )

    if error_id == "AuthenticatedToTelegramAlready":
        error_text = "You are logged in already on a different Telegram account."

    return error_text
