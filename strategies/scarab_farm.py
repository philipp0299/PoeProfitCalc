from bulk_object import BulkObject
from query.modifier import Modifier
from query.modifier_query import ModifierQuery
from strategy import Strategy
from trade_object import TradeObject
from object_lists.evenly_distributed_list import EvenlyDistributedList
from object_lists.least_cost_list import LeastCostList

winged_sextant_farm = None
winged_scarab_exchange = None

gilded_sextant_farm = None
gilded_scarab_exchange = None


def init():
    winged_scarab_sextant = TradeObject(
        ModifierQuery(Modifier("enchant.stat_1697321918"), Modifier("enchant.stat_290368246", vmin=16)))

    winged_scarab_list = [BulkObject("jewelled-bestiary-scarab", "divine"),
                          BulkObject("jewelled-reliquary-scarab", "divine"),
                          BulkObject("jewelled-torment-scarab", "divine"),
                          BulkObject("jewelled-sulphite-scarab", "divine"),
                          BulkObject("jewelled-metamorph-scarab", "divine"),
                          BulkObject("jewelled-legion-scarab", "divine"),
                          BulkObject("jewelled-ambush-scarab", "divine"),
                          BulkObject("winged-blight-scarab", "divine"),
                          BulkObject("jewelled-shaper-scarab", "divine"),
                          BulkObject("winged-expedition-scarab", "divine"),
                          BulkObject("jewelled-harbinger-scarab", "divine"),
                          BulkObject("jewelled-elder-scarab", "divine"),
                          BulkObject("jewelled-divination-scarab", "divine"),
                          BulkObject("jewelled-breach-scarab", "divine"),
                          BulkObject("winged-abyss-scarab", "divine"),
                          BulkObject("jewelled-cartography-scarab", "divine")]

    gilded_scarab_sextant = TradeObject(
        ModifierQuery(Modifier("enchant.stat_1480568810"), Modifier("enchant.stat_290368246", vmin=4)))

    gilded_scarab_list = [BulkObject("gilded-bestiary-scarab", "divine", 5),
                          BulkObject("gilded-reliquary-scarab", "divine", 5),
                          BulkObject("gilded-torment-scarab", "divine", 5),
                          BulkObject("gilded-sulphite-scarab", "divine", 5),
                          BulkObject("gilded-metamorph-scarab", "divine", 5),
                          BulkObject("gilded-legion-scarab", "divine", 5),
                          BulkObject("gilded-ambush-scarab", "divine", 5),
                          BulkObject("gilded-blight-scarab", "divine", 5),
                          BulkObject("gilded-shaper-scarab", "divine", 5),
                          BulkObject("gilded-expedition-scarab", "divine", 5),
                          BulkObject("gilded-harbinger-scarab", "divine", 5),
                          BulkObject("gilded-elder-scarab", "divine", 5),
                          BulkObject("gilded-divination-scarab", "divine", 5),
                          BulkObject("gilded-breach-scarab", "divine", 5),
                          BulkObject("gilded-abyss-scarab", "divine", 5),
                          BulkObject("gilded-cartography-scarab", "divine", 5)]

    winged_sextant_outcome = EvenlyDistributedList(winged_scarab_list, 16 * 3)

    global winged_sextant_farm
    winged_sextant_farm = Strategy(winged_scarab_sextant, winged_sextant_outcome)

    least_cost_scarab_winged = LeastCostList(winged_scarab_list)
    #print(least_cost_scarab_winged.get_least_cost())

    global winged_scarab_exchange
    winged_scarab_exchange = Strategy(least_cost_scarab_winged, EvenlyDistributedList(winged_scarab_list))

    gilded_sextant_outcome = EvenlyDistributedList(gilded_scarab_list, 4 * 3)

    global gilded_sextant_farm
    gilded_sextant_farm = Strategy(gilded_scarab_sextant, gilded_sextant_outcome)

    least_cost_scarab_gilded = LeastCostList(gilded_scarab_list)
    #print(least_cost_scarab_gilded.get_least_cost())

    global gilded_scarab_exchange
    gilded_scarab_exchange = Strategy(least_cost_scarab_gilded, EvenlyDistributedList(gilded_scarab_list))


init()
