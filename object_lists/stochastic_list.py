from currency_amount import CurrencyAmount


class StochasticList:
    def __init__(self, init_list=None, init_chance=1):
        if init_list is None:
            init_list = []
        self.list = init_list
        self.chance = [init_chance] * len(init_list)

    def append(self, item, chance):
        self.list.append(item)
        self.chance.append(chance)
        return self

    def fetch_price(self):
        sum_price = CurrencyAmount(0, "chaos")
        for i in range(len(self.list)):
            sum_price += self.list[i].fetch_price() * self.chance[i]
        return sum_price

    def __str__(self):
        back = ""
        for i in range(len(self.list)):
            if not i == 0:
                back += ", "
            if type(self.list[i]) is CurrencyAmount:
                back += str(self.list[i] * self.chance[i])
            else:
                back += str(self.chance[i]*100) + "% " + str(self.list[i])
        return back
