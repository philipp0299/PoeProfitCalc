from bulk_object import BulkObject
from query.modifier import Modifier
from query.modifier_query import ModifierQuery
from strategy import Strategy
from trade_object import TradeObject
from object_lists.evenly_distributed_list import EvenlyDistributedList
from object_lists.least_cost_list import LeastCostList
import global_items as items

winged_sextant_farm = None
winged_scarab_exchange = None

gilded_sextant_farm = None
gilded_scarab_exchange = None


def init():
    winged_scarab_sextant = TradeObject(
        ModifierQuery(Modifier("enchant.stat_1697321918"), Modifier("enchant.stat_290368246", vmin=16)))


    winged_sextant_outcome = EvenlyDistributedList(items.winged_scarab_list, 16 * 3)

    global winged_sextant_farm
    winged_sextant_farm = Strategy(winged_scarab_sextant, winged_sextant_outcome)

    least_cost_scarab_winged = LeastCostList(items.winged_scarab_list)
    #print(least_cost_scarab_winged.get_least_cost())


    gilded_sextant_outcome = EvenlyDistributedList(items.gilded_scarab_list, 4 * 3)

    global gilded_sextant_farm
    gilded_sextant_farm = Strategy(items.gilded_scarab_sextant, gilded_sextant_outcome)

    least_cost_scarab_gilded = LeastCostList(items.gilded_scarab_list)
    #print(least_cost_scarab_gilded.get_least_cost())

    global gilded_scarab_exchange
    gilded_scarab_exchange = Strategy(least_cost_scarab_gilded, EvenlyDistributedList(items.gilded_scarab_list))


init()
