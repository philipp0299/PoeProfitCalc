# Get custom query from inspecting requests/response from pathoexile.com/trade in browser
# Query is at the bottom of the response
class CustomQuery:
    def __init__(self, query):
        self.query = query

    def get_query_string(self):
        return self.query

