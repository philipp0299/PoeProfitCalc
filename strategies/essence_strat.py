import strategies.global_items as items
import copy

from object_lists.evenly_distributed_list import EvenlyDistributedList
from object_lists.quantity_list import QuantityList
from object_lists.stochastic_list import StochasticList
from strategy import Strategy

change_essence_strat = None


def init():
    global change_essence_strat

    all_deafenings_sorted = copy.copy(items.all_deafenings)

    for item in all_deafenings_sorted:
        item.fetch_price()

    all_deafenings_sorted.sort(key=lambda item: item.fetch_price())

    n_worst = 3
    n_best = 5

    worst_essences = all_deafenings_sorted[0:n_worst]
    best_essences = all_deafenings_sorted[-n_best:-1]
    avg_tries = (len(all_deafenings_sorted) - 1) / n_best

    change_essence_strat = Strategy(QuantityList().append(EvenlyDistributedList(worst_essences), 1)
                                    .append(items.primal_lifeforce, 30 * avg_tries),
                                    EvenlyDistributedList(best_essences))


init()
