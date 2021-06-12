
def handle_error(chat_id, error_id, context):
    error_text = "I'm sorry. I encountered an error carrying out that operation. Try again later and I should have it all sorted out."
    if error_id == 'AuthenticationFailed':
        error_text = 'Hmmm. I cannot find a Maui user with email and password you entered.'
    return context.bot.send_message(chat_id=chat_id, text=error_text)