from gql import Client
from gql.transport.requests import RequestsHTTPTransport
from utilities.tokens import get as get_tokens
import config

def get(telegram_id):
    transport = RequestsHTTPTransport(
        url = config.get('api_url'),
        use_json = True,
        headers = get_headers(telegram_id),
        verify = False,
        retries = 3,
    )
    client = Client(
        transport = transport,
        fetch_schema_from_transport = True,
    )
    return client

def get_headers(telegram_id):
    headers = { "Content-Type": "application/json" }
    tokens = get_tokens()
    token = tokens.get(telegram_id)
    if token:
        headers['Authorization'] = "Bearer " + token
    return headers