from gql import gql

LOGIN = gql(
    """
        mutation TelegramLogin($email: String!, $password: String!, $telegram_id: String!) {
            telegramLogin(email: $email, password: $password, telegram_id: $telegram_id) {
                message
                user {
                    id
                    name
                    email
                    currency
                }
                errorId
                token
            }
        }
        """
)

LOGOUT = gql(
    """ 
        mutation TelegramLogout {
            telegramLogout {
                message
            }
        }
        """
)
