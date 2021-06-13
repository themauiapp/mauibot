from gql import gql

LOGIN = gql('''
        mutation StatelessLogin($email: String!, $password: String!, $telegram_id: String!) {
            statelessLogin(email: $email, password: $password, telegram_id: $telegram_id) {
                message
                user {
                    name
                    email
                }
                errorId
                token
            }
        }
        ''')