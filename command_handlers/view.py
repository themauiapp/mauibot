from utilities.actions import record as record_action
import packages.calendar as calendar

def view_handler(update, context): 
    chat_id = str(update.effective_chat.id)
    text = 'Cool. What date do you want to view expenses for ?'
    record_action(chat_id, 'view')
    context.bot.send_message(chat_id=chat_id, text=text, reply_markup=calendar.create_calendar())