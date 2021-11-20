import os.path as path
import json
import config


def get_actions_path():
    app_root = config.get("app_root")
    actions_path = path.join(app_root, "storage", "actions.json")
    return actions_path


def get():
    with open(get_actions_path(), "r") as reader:
        actions = json.load(reader)
    return actions


def set(actions, telegram_id, action):
    actions[telegram_id] = action
    with open(get_actions_path(), "w") as writer:
        json.dump(actions, writer)


def record(telegram_id, action):
    actions = get()
    set(actions, telegram_id, action)


def get_latest(telegram_id):
    actions = get()
    return actions[telegram_id]
