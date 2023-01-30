import requests
import json
import ratelimited_requests
from currency_amount import CurrencyAmount


class TradeObject:
    def __init__(self, query):
        self.query = query.get_query_string()
        self.price = None

    def fetch_price(self):
        if self.price is None:
            headers = {'User-Agent': 'PoeProfitCalc (https://github.com/Dakri7/PoeProfitCalc.git)', 'accept': 'application/json'}
            # TODO current league
            api_endpoint = "http://www.pathofexile.com/api/trade/search/Sanctum"
            query_response = ratelimited_requests.post(api_endpoint, json=self.query, headers=headers)
            query_data = json.loads(query_response.content)

            item_id = query_data['result'][0]
            query_id = query_data['id']
            item_url = "https://www.pathofexile.com/api/trade/fetch/" + item_id + "?query=" + query_id
            item_response = ratelimited_requests.get(item_url, headers=headers)
            item_data = json.loads(item_response.content)
            price = item_data['result'][0]['listing']['price']
            self.price = CurrencyAmount(price['amount'], price['currency'])
        return self.price
