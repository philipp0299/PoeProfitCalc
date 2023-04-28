from query.name_query import NameQuery
from query.type_query import TypeQuery
from trade_object import TradeObject
from object_lists.quantity_list import QuantityList
from strategy import Strategy
from query.modifier import Modifier
from query.modifier_query import ModifierQuery
import strategies.crafting as crafting
import strategies.misc_strats as misc_strats
import strategies.essence_strat as essence_strats
import strategies.reroll_strategy


#print("Scarab Exchange:", scarab_farms.gilded_scarab_exchange.calc_profit())
#print("Scarab Farm:", scarab_farms.gilded_sextant_farm.calc_profit())

#print("Crafting RF Helmet", crafting.finish_rf_helmet_strat.calc_profit())

#print("Crafting Diamond Flask", crafting.finish_diamond_flask_strat.calc_profit())

#print("Double Corrupt Squires", misc_strats.double_corrupt_squire_strat.calc_profit())
#print(misc_strats.double_corrupt_squire_strat.calc_min_rounds_for_profit(0.8, 0))
#print(essence_strats.change_essence_strat.calc_profit())
#print(essence_strats.change_essence_strat)

print(strategies.reroll_strategy.breachstone_exchange.get_worst_items())
print(strategies.reroll_strategy.breachstone_exchange.calc_profit())


