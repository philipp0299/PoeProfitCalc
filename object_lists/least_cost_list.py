from currency_amount import CurrencyAmount


class LeastCostList:
    def __init__(self, init_list=[]):
        self.list = init_list
        self.least_cost = None

    def append(self, item, quantity=1):
        self.list.append(item)
        return self

    def fetch_price(self):
        least_price = self.list[0].fetch_price()
        self.least_cost = self.list[0]
        for i in range(len(self.list)):
            if self.list[i].fetch_price() < least_price:
                least_price = self.list[i].fetch_price()
                self.least_cost = self.list[i]
        return least_price

    def get_least_cost(self):
        if self.least_cost is None:
            self.fetch_price()
        return self.least_cost
