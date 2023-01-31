class NameQuery:

    def __init__(self, name):
        self.name = name

    def get_query_string(self):
        return {
            "query": {
                "status": {
                    "option": "online"
                },
                "name": self.name,
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
        return self.name
