from gql import gql

DAILYEXPENSES = gql('''
        query DailyExpenses($date: String!, $all: Boolean) {
            dailyExpenses(date: $date, all: $all) {
                expenses {
                    name
                    amount
                }
                sum
                pagination {
                    currentPage
                    maxPages
                }
            }
        }
    ''')