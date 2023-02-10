from currency_amount import CurrencyAmount
from object_lists.quantity_list import QuantityList


class StochasticlyIndependentList(QuantityList):

    def __init__(self, init_list=None, init_count=0):
        QuantityList.__init__(self, init_list, init_count)

    def __str__(self):
        back = ""
        for i in range(len(self.list)):
            if not i == 0:
                back += ", "
            if type(self.list[i]) is CurrencyAmount:
                back += str(self.list[i] * self.quantity[i])
            else:
                back += str(self.quantity[i]*100) + "% " + str(self.list[i])
        return back
