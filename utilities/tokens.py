import os.path as path
import json
import config

def get_tokens_path():
    app_root = config.get('app_root')
    tokens_path = path.join(app_root, 'storage', 'tokens.json')
    return tokens_path

def get():
    with open(get_tokens_path(), 'r') as reader:
        tokens = json.load(reader)
    return tokens

def set(tokens, telegram_id=None, token=None):
    if telegram_id is not None:
        tokens[telegram_id] = token
    with open(get_tokens_path(), 'w') as writer: 
        json.dump(tokens, writer)

def record(telegram_id, token):
    tokens = get()
    set(tokens, telegram_id, token)

def delete(telegram_id):
    tokens = get()
    del tokens[telegram_id]
    set(tokens)
