from bulk_object import BulkObject
from object_lists.quantity_list import QuantityList
from object_lists.stochastic_list import StochasticList
from query.custom_query import CustomQuery
from strategy import Strategy
from trade_object import TradeObject

shaper_farm = None
elder_farm = None
uber_elder_farm = None

def init():
    hydra = BulkObject("hydra", "chaos", 5)
    phoenix = BulkObject("phoenix", "chaos", 5)
    chimera = BulkObject("chimer", "chaos", 5)
    minotaur = BulkObject("minot", "chaos", 5)
    shaper_frags = QuantityList().append(hydra).append(phoenix).append(chimera).append(minotaur)
    knowledge = BulkObject("fragment-of-knowledge", "chaos", 2)
    shape = BulkObject("fragment-of-shape", "chaos", 2)
    uber_elder_frags_shaper = StochasticList().append(knowledge, 0.5).append(shape, 0.5)

    global shaper_farm
    shaper_farm = Strategy(shaper_frags, uber_elder_frags_shaper)

    #print("Shaper farm: ", shaper_farm.calc_profit())

    enslave = BulkObject("fragment-of-enslavement", "chaos", 5)
    erad = BulkObject("fragment-of-eradication", "chaos", 5)
    constric = BulkObject("fragment-of-constriction", "chaos", 5)
    puri = BulkObject("fragment-of-purification", "chaos", 5)

    elder_frags = QuantityList().append(enslave).append(erad).append(constric).append(puri)

    terror = BulkObject("fragment-of-terror", "chaos", 2)
    emptiness = BulkObject("fragment-of-emptiness", "chaos", 2)

    unid_watchers_eye = TradeObject(CustomQuery({"query": {
            "name": "Watcher's Eye",
            "type": "Prismatic Jewel",
            "stats": [
                {
                    "type": "and",
                    "filters": [],
                    "disabled": False
                }
            ],
            "status": "online",
            "filters": {
                "misc_filters": {
                    "filters": {
                        "identified": {
                            "option": "false"
                        }
                    },
                    "disabled": False
                }
            }
        }
    }))

    elder_drops = StochasticList().append(terror, 0.5).append(emptiness, 0.5).append(unid_watchers_eye, 0.35)

    global elder_farm
    elder_farm = Strategy(elder_frags, elder_drops)

    #print("Elder farm: ", elder_farm.calc_profit())

    uber_elder_frags = QuantityList().append(shape).append(knowledge).append(terror).append(emptiness)

    unid_watchers_eye_i86 = TradeObject(CustomQuery({"query": {
            "name": "Watcher's Eye",
            "type": "Prismatic Jewel",
            "stats": [
                {
                    "type": "and",
                    "filters": [],
                    "disabled": False
                }
            ],
            "status": "online",
            "filters": {
                "misc_filters": {
                    "filters": {
                        "ilvl": {
                            "min": 86,
                            "max": None
                        },
                        "identified": {
                            "option": "false"
                        }
                    },
                    "disabled": False
                }
            }
        }
    }))

    uber_elder_drops = StochasticList().append(unid_watchers_eye_i86, 0.35)

    global uber_elder_farm
    uber_elder_farm = Strategy(uber_elder_frags, uber_elder_drops)
    #print("Uber Elder farm: ", uber_elder_farm.calc_profit())


init()
