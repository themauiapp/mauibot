from gql import gql

FETCHUSERSTONOTIFY = gql(
    """
        query UsersByTelegramSetting($time: String!) {
            usersByTelegramSetting(time: $time) {
                telegram {
                    telegram_id
                }
            }
        }
        """
)
