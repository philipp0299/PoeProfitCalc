import itertools
from object_lists.quantity_list import QuantityList
from scipy.stats import multinomial
from currency_amount import CurrencyAmount


class StochasticlyExclusiveList(QuantityList):
    def __init__(self, init_list=None, init_count=0):
        QuantityList.__init__(self, init_list, init_count)
        self.pi = list(map(lambda x: x.fetch_price().converted_amount("chaos"), self.list))
        if sum(self.quantity) > 1:
            raise RuntimeError("Probability of mutually exclusive events exceed 1")

    def append(self, item, quantity=1):
        super().append(item, quantity)
        self.pi = list(map(lambda x: x.fetch_price().converted_amount("chaos"), self.list))
        if sum(self.quantity) > 1:
            raise RuntimeError("Probability of mutually exclusive events exceed 1")
        return self

    def calc_min_rounds_for_profit(self, certainty, spendings_per_trial, min_profit=0):
        #TODO more efficient algorithm
        n = 1
        spendings = spendings_per_trial.fetch_price().converted_amount("chaos")
        while self.chance_for_profit(n, spendings, min_profit) < certainty:
            n += 1
        return n

    def chance_for_profit(self, n, spendings_per_trial, min_profit):
        if type(spendings_per_trial) is CurrencyAmount:
            spendings_per_trial = spendings_per_trial.fetch_price().converted_amount("chaos")
        profits = [x_i - spendings_per_trial for x_i in self.pi]
        profits.append(-spendings_per_trial)    # Append an outcome that looses all money spent
        array = list(filter(lambda x: sum(x) == n, itertools.product(range(0, n + 1), repeat=len(profits))))
        profit_combs = list(filter(lambda x: sum(x_1 * y_i for x_1, y_i in zip(x, profits)) >= min_profit, array))
        p = self.quantity[:]
        p.append(1 - sum(self.quantity))    # Probability for the "loose all" event is equal to the rest
        rv = multinomial(n, p)
        profit_combs_probs = list(map(rv.pmf, profit_combs))
        return sum(profit_combs_probs)

