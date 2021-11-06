from dotenv import load_dotenv
import os

config = {}


def set():
    global config
    app_root = os.path.dirname(__file__)
    env_path = os.path.join(app_root, ".env")
    load_dotenv(env_path)
    config = {
        "app_root": app_root,
        "bot_token": os.environ.get("BOT_TOKEN"),
        "api_url": os.environ.get("GRAPHQL_API_URL"),
    }


def get(key):
    return config.get(key)
