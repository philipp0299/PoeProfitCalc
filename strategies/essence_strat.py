import strategies.global_items as items
import copy

from object_lists.evenly_distributed_list import EvenlyDistributedList
from object_lists.quantity_list import QuantityList
from object_lists.stochasticly_independent_list import StochasticlyIndependentList
from strategy import Strategy
from currency_amount import CurrencyAmount
from strategies.reroll_strategy import RerollStrategy

change_essence_strat = None


def init():
    global change_essence_strat

    change_essence_strat = RerollStrategy(items.all_deafenings, QuantityList().append(items.primal_lifeforce, 30))

init()
