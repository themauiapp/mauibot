from os import environ
from utilities.error_handler import handle_error

import requests
import sys

def trigger_agape_email(context):
    url = environ.get("AGAPE_URL")

    try:
        response = requests.post(url)
        print(response)
        response.raise_for_status()
    except Exception as exception:
        exception = sys.exc_info()
        handle_error(None, None, exception)

