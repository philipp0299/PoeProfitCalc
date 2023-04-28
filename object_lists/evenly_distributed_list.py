from currency_amount import CurrencyAmount


class EvenlyDistributedList:
    def __init__(self, init_list=[], count_drops=1):
        self.list = init_list
        self.count_drops = count_drops

    def append(self, item):
        self.list.append(item)
        return self

    def fetch_price(self):
        sum_price = CurrencyAmount(0, "chaos")
        for i in range(len(self.list)):
            sum_price += self.list[i].fetch_price() * (1 / len(self.list))
        return sum_price * self.count_drops

    def __str__(self):
        back = ""
        for i in range(len(self.list)):
            if not i == 0:
                back += ", "
            if type(self.list[i]) is CurrencyAmount:
                back += str(self.list[i] * self.quantity[i])
            else:
                back += str(self.list[i])
        return back
