from object_lists.quantity_list import QuantityList
from query.modifier import Modifier
from query.modifier_query import ModifierQuery
from query.name_query import NameQuery
from query.type_query import TypeQuery
from strategy import Strategy
from trade_object import TradeObject

spirit_drinker_upgrade_strat = None

def init()
    stitched_demon = TradeObject(NameQuery("Mask of the Stitched Demon"))
    spirit_drinker = TradeObject(NameQuery("Mask of the Spirit Drinker"))
    summoning_vial = TradeObject(TypeQuery("Vial of Summoning"))
    apex_of_sacrifice = TradeObject(ModifierQuery(Modifier("pseudo.pseudo_temple_sacrifice_room_3", option=1)))
    lst = QuantityList().append(spirit_drinker).append(summoning_vial).append(apex_of_sacrifice)

    global spirit_drinker_upgrade_strat
    spirit_drinker_upgrade_strat = Strategy(lst, stitched_demon)

init()