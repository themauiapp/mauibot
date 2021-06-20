import os.path as path
import json
import config

def get_expenses_path():
    app_root = config.get('app_root')
    expenses_path = path.join(app_root, 'storage', 'expenses.json')
    return expenses_path

def get():
    with open(get_expenses_path(), 'r') as reader:
        expenses = json.load(reader)
    return expenses

def set(expenses, telegram_id, expense):
    expenses[telegram_id] = expense
    with open(get_expenses_path(), 'w') as writer: 
        json.dump(expenses, writer)

def record(telegram_id, expense):
    expenses = get()
    set(expenses, telegram_id, expense)
