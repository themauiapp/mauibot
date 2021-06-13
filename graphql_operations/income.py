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