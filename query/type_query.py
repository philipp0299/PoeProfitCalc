class TypeQuery:

    def __init__(self, type):
        self.type = type

    def get_query_string(self):
        return {
            "query": {
                "status": {
                    "option": "online"
                },
                "type": self.type,
                "stats": [{
                    "type": "and",
                    "filters": []
                }],
                "filters": {
                    "trade_filters": {
                        "collapse": True
                    }
                }
            },
            "sort": {
                "price": "asc"
            }
        }

    def __str__(self):
        return self.type
