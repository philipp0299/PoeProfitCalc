from query.custom_query import CustomQuery
from query.name_query import NameQuery
from query.type_query import TypeQuery
from trade_object import TradeObject
from object_lists.quantity_list import QuantityList
from strategy import Strategy
from bulk_object import BulkObject
from object_lists.stochastic_list import StochasticList
from modifier import Modifier
from query.modifier_query import ModifierQuery
import strategies.boss_farms as boss_farms
import strategies.scarab_farm as scarab_farms

stitched_demon = TradeObject(NameQuery("Mask of the Stitched Demon"))
spirit_drinker = TradeObject(NameQuery("Mask of the Spirit Drinker"))
summoning_vial = TradeObject(TypeQuery("Vial of Summoning"))
apex_of_sacrifice = TradeObject(CustomQuery(
    {
        "query": {
            "stats": [
                {
                    "type": "and",
                    "filters": [
                        {
                            "id": "pseudo.pseudo_temple_sacrifice_room_3",
                            "disabled": False,
                            "value": {
                                "option": 1
                            }
                        }
                    ],
                    "disabled": False
                }
            ],
            "status": "online"
        }
    }))
lst = QuantityList().append(spirit_drinker).append(summoning_vial).append(apex_of_sacrifice)

strat = Strategy(lst, stitched_demon)

print("Temple Upgrade Stitched Demon: ", strat.calc_profit())


#print("Scarab Exchange:", scarab_farms.gilded_scarab_exchange.calc_profit())
#print("Scarab Farm:", scarab_farms.gilded_sextant_farm.calc_profit())



