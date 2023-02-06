from object_lists.quantity_list import QuantityList
from query.modifier import Modifier
from query.modifier_query import ModifierQuery
from query.name_query import NameQuery
from query.type_query import TypeQuery
from strategy import Strategy
from trade_object import TradeObject
import query.modifier as modifier
from object_lists.stochastic_list import StochasticList

spirit_drinker_upgrade_strat = None
double_corrupt_squire_strat = None

def init():
    global spirit_drinker_upgrade_strat
    stitched_demon = TradeObject(NameQuery("Mask of the Stitched Demon"))
    spirit_drinker = TradeObject(NameQuery("Mask of the Spirit Drinker"))
    summoning_vial = TradeObject(TypeQuery("Vial of Summoning"))
    apex_of_sacrifice = TradeObject(ModifierQuery(Modifier("pseudo.pseudo_temple_sacrifice_room_3", option=1)))
    lst = QuantityList().append(spirit_drinker).append(summoning_vial).append(apex_of_sacrifice)

    spirit_drinker_upgrade_strat = Strategy(lst, stitched_demon)

    global double_corrupt_squire_strat
    shieldbearer = TradeObject(TypeQuery("The Shieldbearer"), nth_result=7)
    squire = TradeObject(NameQuery("The Squire"))

    plus_one_squire = TradeObject(ModifierQuery(modifier.from_text("# to Level of Socketed Gems", "implicit")))

    double_corrupt_squire_strat = Strategy(QuantityList().append(shieldbearer, 8),
                                           StochasticList().append(squire, 0.25 + (0.25 * 0.6)).append(plus_one_squire, 0.25 * 0.4))
init()