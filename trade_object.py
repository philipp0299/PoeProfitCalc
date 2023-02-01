import sys

import requests
import json

import league
import ratelimited_requests
from currency_amount import CurrencyAmount


class TradeObject:
    def __init__(self, query, nth_result=0):
        self.query = query
        self.price = None
        self.nth_result = nth_result

    def fetch_price(self):
        if self.price is None:
            headers = {'User-Agent': 'PoeProfitCalc (https://github.com/Dakri7/PoeProfitCalc.git)', 'accept': 'application/json'}
            curr_league = league.get_current_league()
            api_endpoint = "http://www.pathofexile.com/api/trade/search/" + curr_league
            query_string = self.query.get_query_string()
            query_response = ratelimited_requests.post(api_endpoint, json=query_string, headers=headers)
            if query_response.status_code == requests.codes.bad_request:
                sys.stderr.write("Item with this data not found. Assuming value of 0. This is not correct! \n")
                return CurrencyAmount(0, "divine")
            query_data = json.loads(query_response.content)

            if len(query_data['result']) == 0:
                sys.stderr.write("No item found for the given mods. Assuming value of 0. This is not correct! \n")
                return CurrencyAmount(0, "divine")
            item_id = query_data['result'][self.nth_result]

            query_id = query_data['id']
            item_url = "https://www.pathofexile.com/api/trade/fetch/" + item_id + "?query=" + query_id
            item_response = ratelimited_requests.get(item_url, headers=headers)
            item_data = json.loads(item_response.content)
            price = item_data['result'][0]['listing']['price']
            self.price = CurrencyAmount(price['amount'], price['currency'])
        return self.price

    def __str__(self):
        if self.price is None:
            return str(self.query)
        else:
            return str(self.query) + " for " + str(self.price)
