from query.name_query import NameQuery
from query.type_query import TypeQuery
from trade_object import TradeObject
from object_lists.quantity_list import QuantityList
from strategy import Strategy
from query.modifier import Modifier
from query.modifier_query import ModifierQuery
import strategies.crafting as crafting


#print("Temple Upgrade Stitched Demon: ", strat.calc_profit())

#print("Scarab Exchange:", scarab_farms.gilded_scarab_exchange.calc_profit())
#print("Scarab Farm:", scarab_farms.gilded_sextant_farm.calc_profit())

print("Crafting RF Helmet", crafting.finish_rf_helmet_strat.calc_profit())

print("Crafting Diamond Flask", crafting.finish_diamond_flask_strat.calc_profit())



