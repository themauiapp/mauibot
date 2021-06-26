from gql import gql

CURRENTMONTHINCOME = gql(''' 
        query CurrentMonthIncome {
            currentMonthIncome {
                total
                remainder
                percent_remainder
                expenses_count
            }
        }
    ''')

INCOMESTATS = gql('''
        query IncomeStats {
            incomeStats {
                income_total
                income_spent
                income_remainder
            }
        }
    ''')