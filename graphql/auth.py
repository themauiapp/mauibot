from gql import gql

LOGIN = gql('''
        mutation StatelessLogin($email: String!, $password: String!) {
            statelessLogin(email: $email, password: $password) {
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