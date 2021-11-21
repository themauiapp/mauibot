from dotenv import load_dotenv
import os

app_root = os.path.dirname(__file__)

def set():
    env_path = os.path.join(app_root, ".env")
    load_dotenv(env_path)

def get(key=None):
    config = {
        "app_root": app_root,
        "bot_token": os.environ.get("BOT_TOKEN"),
        "api_url": os.environ.get("GRAPHQL_API_URL"),
    }
    return config if not key else config.get(key)
