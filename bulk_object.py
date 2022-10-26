import requests
import json
from currency_amount import CurrencyAmount
import ratelimited_requests


class BulkObject:
    def __init__(self, obj_tag, cost_tag, min_quantity=1):
        self.obj_tag = obj_tag
        self.cost_tag = cost_tag
        self.min_quantity = min_quantity
        self.price = None

    def fetch_price(self):
        if self.price is None:
            query = {
                "exchange": {
                    "have": [self.cost_tag],
                    "want": [self.obj_tag],
                    "minimum": self.min_quantity,
                    "status": {
                        "option": "online"
                    }
                }
            }

            headers = {'User-Agent': 'PoeProfitCalc (https://github.com/Dakri7/PoeProfitCalc.git)', 'accept': 'application/json'}
            # TODO current league
            api_endpoint = "http://www.pathofexile.com/api/trade/exchange/Kalandra"
            query_response = ratelimited_requests.post(api_endpoint, json=query, headers=headers)
            query_data = json.loads(query_response.content)
            first_listing = list(query_data["result"].values())[0]
            listing_data = first_listing["listing"]["offers"][0]
            obj_amount = listing_data['item']['amount']
            cost_for_all = listing_data['exchange']["amount"]
            self.price = CurrencyAmount(cost_for_all / obj_amount, self.cost_tag)
        return self.price

