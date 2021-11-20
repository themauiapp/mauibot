from datetime import datetime
import os.path as path
from config import get as get_config
import json

logs_path = path.join(get_config().get("app_root"), "storage", "logs.json")


def record(error):
    with open(logs_path, "r") as reader:
        data = json.load(reader)
    new_logs = data.get("logs")
    new_logs.insert(0, {get_timestamp(): error})
    new_data = {"logs": new_logs}
    set(new_data)


def set(data):
    with open(logs_path, "w") as writer:
        json.dump(data, writer)


def get_timestamp():
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")
