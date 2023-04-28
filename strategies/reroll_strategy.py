from currency_amount import CurrencyAmount
from object_lists.evenly_distributed_list import EvenlyDistributedList
from object_lists.quantity_list import QuantityList
from strategy import Strategy
import strategies.global_items as items


class RerollStrategy(Strategy):

    def __init__(self, all_items, reroll_cost, exclude_self=True):
        self.all_items = all_items
        self.reroll_cost = reroll_cost
        self.exclude_self = exclude_self
        self.profit = None
        self.worst = None
        Strategy.__init__(self, None, None)

    def calc_profit(self):
        self.calculate_worst()
        return Strategy.calc_profit(self)

    def calculate_worst(self):
        combined_cost = CurrencyAmount(0, "chaos")
        for it in self.all_items:
            combined_cost += it.fetch_price()
        lifeforce_price = self.reroll_cost.fetch_price()
        self.worst = EvenlyDistributedList()
        for it in self.all_items:
            # Can the item reroll into itself
            if self.exclude_self:
                to_beat = (combined_cost - it.fetch_price()) * (1 / (len(self.all_items) - 1))
            else:
                to_beat = combined_cost * (1 / len(self.all_items))
            if it.fetch_price() + lifeforce_price < to_beat:
                self.worst.append(it)
        self.educts = QuantityList().append(self.worst, 1).append(self.reroll_cost)
        self.products = EvenlyDistributedList(self.all_items)

    def get_worst_items(self):
        self.calculate_worst()
        return self.worst


winged_scarab_exchange = None
gilded_scarab_exchange = None
breachstone_exchange = None


def init():
    global winged_scarab_exchange
    winged_scarab_exchange = RerollStrategy(items.winged_scarab_list, QuantityList().append(items.wild_lifeforce, 30))
    global gilded_scarab_exchange
    gilded_scarab_exchange = RerollStrategy(items.gilded_scarab_list, QuantityList().append(items.wild_lifeforce, 30))
    global breachstone_exchange
    breachstone_exchange = RerollStrategy(items.breachstone_list, QuantityList().append(items.wild_lifeforce, 30))

init()

