from currency_amount import CurrencyAmount


class QuantityList:
    def __init__(self, init_list=None, init_count=1):
        if init_list is None:
            init_list = []
        self.list = init_list
        self.quantity = [init_count] * len(init_list)

    def append(self, item, quantity=1):
        self.list.append(item)
        self.quantity.append(quantity)
        return self

    def fetch_price(self):
        sum_price = CurrencyAmount(0, "chaos")
        for i in range(len(self.list)):
            sum_price += self.list[i].fetch_price() * self.quantity[i]
        return sum_price

    def __str__(self):
        back = ""
        for i in range(len(self.list)):
            if not i == 0:
                back += " + "
            if type(self.list[i]) is CurrencyAmount:
                back += str(self.list[i] * self.quantity[i])
            else:
                back += str(self.quantity[i]) + "x" + str(self.list[i])
        return back
