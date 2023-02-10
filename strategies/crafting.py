import json

from query.filter import Filter
from query.modifier_query import ModifierQuery
from query.modifier import Modifier
from query.name_query import NameQuery
from query.type_query import TypeQuery
from trade_object import TradeObject
from strategy import Strategy
from object_lists.stochasticly_independent_list import StochasticlyIndependentList
from currency_amount import CurrencyAmount
import query.modifier as modifier

finish_rf_helmet_strat = None
finish_diamond_flask_strat = None

one_mod = 0.65
two_mod = 0.25
three_mod = 0.1


def init():
    global finish_rf_helmet_strat
    global finish_diamond_flask_strat

    uncrafted_rf_helmet = TradeObject(ModifierQuery(
        Filter(
            [modifier.from_text("Socketed Gems are Supported by Level # Burning Damage", vmin=20),
             modifier.from_text("Socketed Gems deal #% more Elemental Damage")],
            filter_type="and"),
        Filter(
            [modifier.from_text("# Crafted Prefix Modifiers", mod_type="pseudo", vmin=1),
             modifier.from_text("# Prefix Modifiers", mod_type="pseudo", vmax=2)],
            filter_type="count", filter_value_min=1),
        base_type="Royal Burgonet"))

    finished_rf_helmet = TradeObject(ModifierQuery(
        Filter(
            [modifier.from_text("Socketed Gems are Supported by Level # Burning Damage", vmin=20),
             modifier.from_text("Socketed Gems deal #% more Elemental Damage"),
             modifier.from_text("# to Level of Socketed AoE Gems", vmin=2),
             modifier.from_text("+# total maximum Life", mod_type="pseudo")],
            filter_type="and"),
        base_type="Royal Burgonet"))

    meta_craft_beast = TradeObject(TypeQuery("Wild Bristle Matron"))

    chance_to_fail = three_mod * (1 - 0.377)  # 0.377 is the chance to hit +2 without a crafted mod

    finish_rf_helmet_strat = Strategy(
        StochasticlyIndependentList()
        .append(meta_craft_beast, 2.29)
        .append(CurrencyAmount(1, "veiled-chaos-orb"), 2.29)
        .append(CurrencyAmount(4, "chaos"), 2.29)  # craft cost of + number of zombies/skeletons
        .append(uncrafted_rf_helmet, 1 + (chance_to_fail * 2.29)),
        finished_rf_helmet)

    unfinished_diamond_flask = TradeObject(ModifierQuery(modifier.from_text("#% increased Critical Strike Chance during Flask Effect", vmin=50),
                                                         modifier.from_text("# Empty Prefix Modifiers", mod_type="pseudo", vmin=1),
                                                         base_type="Diamond Flask"))

    finished_diamond_flask = TradeObject(ModifierQuery(modifier.from_text("#% increased Critical Strike Chance during Flask Effect", vmin=50),
                                                       modifier.from_text("#% increased effect", mod_type="enchant", vmin=70),
                                                       modifier.from_text("#% increased effect"),
                                                       base_type="Diamond Flask"), nth_result=2)

    finish_diamond_flask_strat = Strategy(StochasticlyIndependentList().append(unfinished_diamond_flask, 1)
                                          .append(CurrencyAmount(1, "enkindling-orb"), 26),
                                          StochasticlyIndependentList().append(finished_diamond_flask, 0.13514))



init()
