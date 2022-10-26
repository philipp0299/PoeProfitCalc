from currency_amount import CurrencyAmount


class StochasticList:
    def __init__(self, init_list=[]):
        self.list = init_list
        self.chance = []

    def append(self, item, chance):
        self.list.append(item)
        self.chance.append(chance)
        return self

    def fetch_price(self):
        sum_price = CurrencyAmount(0, "chaos")
        for i in range(len(self.list)):
            sum_price += self.list[i].fetch_price() * self.chance[i]
        return sum_price
