from query.custom_query import CustomQuery
from trade_object import TradeObject
from strategy import Strategy
from object_lists.stochastic_list import StochasticList
from object_lists.quantity_list import QuantityList
from currency_amount import CurrencyAmount


def init():
    uncrafted_rf_helmet= TradeObject(CustomQuery({"query": {
            "type": "Eternal Burgonet",
            "stats": [
                {
                    "type": "and",
                    "filters": [
                        {
                            "id": "explicit.stat_2680613507",
                            "disabled": False,
							"value": {
                                "min": 1
                            }
                        },
                        {
                            "id": "explicit.stat_3835899275",
                            "disabled": False,
							"value": {
                                "min": 1
                            }
                        }
                    ],
                    "disabled": False
                },
                {
                    "type": "count",
                    "filters": [
                        {
                            "id": "pseudo.pseudo_number_of_crafted_prefix_mods",
                            "disabled": False,
                            "value": {
                                "min": 1
                            }
                        },
                        {
                            "id": "pseudo.pseudo_number_of_prefix_mods",
                            "disabled": False,
                            "value": {
                                "max": 2
                            }
                        }
                    ],
                    "disabled": False,
                    "value": {
                        "min": 1
                    }
                }
            ],
            "status": "online",
            "filters": {
                "type_filters": {
                    "filters": {
                        "category": {
                            "option": "armour.helmet"
                        }
                    },
                    "disabled": False
                }
            }
        }
    }))

    finished_rf_helmet = TradeObject(CustomQuery({"query": {
        "type": "Eternal Burgonet",
        "stats": [
            {
                "type": "and",
                "filters": [
                    {
                        "id": "explicit.stat_2680613507",
                        "disabled": False,
                        "value": {
                            "min": 0
                        }
                    },
                    {
                        "id": "explicit.stat_3835899275",
                        "disabled": False,
                        "value": {
                            "min": 0
                        }
                    },
                    {
                        "id": "explicit.stat_2551600084",
                        "disabled": False,
                        "value": {
                            "min": 2
                        }
                    }
                ],
                "disabled": False
            }
        ],
        "status": "online",
        "filters": {
            "type_filters": {
                "filters": {
                    "category": {
                        "option": "armour.helmet"
                    }
                },
                "disabled": False
            }
        }
    }}))


    finish_rf_helmet_strat = Strategy(StochasticList().append( CurrencyAmount(2, "divine"), 2.29).append(CurrencyAmount(1, "veiled-chaos-orb"), 2.29).append(uncrafted_rf_helmet, 1), finished_rf_helmet)
    print(finish_rf_helmet_strat.calc_profit())