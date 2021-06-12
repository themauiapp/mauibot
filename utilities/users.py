import os.path as path
import json
import config

def get_users_path():
    app_root = config.get('app_root')
    users_path = path.join(app_root, 'storage', 'users.json')
    return users_path

def get():
    with open(get_users_path(), 'r') as reader:
        users = json.load(reader)
    return users

def set(users, telegram_id, user):
    users[telegram_id] = user
    with open(get_users_path(), 'w') as writer: 
        json.dump(users, writer)

def record(telegram_id, user):
    users = get()
    set(users, telegram_id, user)