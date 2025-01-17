from currency_amount import CurrencyAmount
from object_lists.stochasticly_exclusive_list import StochasticlyExclusiveList

class Strategy:
    def __init__(self, educts, products, time=None):
        self.educts = educts
        self.products = products
        self.time = time

    def calc_profit(self):
        educt_cost = self.educts.fetch_price()
        product_cost = self.products.fetch_price()
        profit = product_cost - educt_cost
        if profit > CurrencyAmount(0.5, "divine"):
            profit.change_type("divine")
        if profit > CurrencyAmount(0.5, "mirror"):
            profit.change_type("mirror")
        return profit

    def __str__(self):
        return str(self.educts) + " => " + str(self.products)

    def calc_min_rounds_for_profit(self, certainty, min_profit=0):
        if type(self.products) is StochasticlyExclusiveList:
            return self.products.calc_min_rounds_for_profit(certainty, self.educts.fetch_price(), min_profit)
        else:
            return 0

    # TODO: Printable instructions with trade links
