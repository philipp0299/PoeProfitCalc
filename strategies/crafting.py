import json

from query.filter import Filter
from query.modifier_query import ModifierQuery
from query.modifier import Modifier
from query.name_query import NameQuery
from query.type_query import TypeQuery
from trade_object import TradeObject
from strategy import Strategy
from object_lists.stochastic_list import StochasticList
from currency_amount import CurrencyAmount

finish_rf_helmet_strat = None
finish_diamond_flask_strat = None

one_mod = 0.65
two_mod = 0.25
three_mod = 0.1

pseudo_modifiers = {}
explicit_modifiers = {}
implicit_modifiers = {}
fractured_modifiers = {}
enchant_modifiers = {}
crafted_modifiers = {}
veiled_modifiers = {}
monster_modifiers = {}
delve_modifiers = {}
ultimatum_modifiers = {}


def init():
    parse_modifier_list()
    global finish_rf_helmet_strat
    global finish_diamond_flask_strat

    uncrafted_rf_helmet = TradeObject(ModifierQuery(
        Filter(
            [Modifier(explicit_modifiers["Socketed Gems are Supported by Level # Burning Damage"], vmin=20),
             Modifier(explicit_modifiers["Socketed Gems deal #% more Elemental Damage"])],
            filter_type="and"),
        Filter(
            [Modifier(pseudo_modifiers["# Crafted Prefix Modifiers"], vmin=1),
             Modifier(pseudo_modifiers["# Prefix Modifiers"], vmax=2)],
            filter_type="count", filter_value_min=1),
        base_type="Royal Burgonet"))

    finished_rf_helmet = TradeObject(ModifierQuery(
        Filter(
            [Modifier(explicit_modifiers["Socketed Gems are Supported by Level # Burning Damage"], vmin=20),
             Modifier(explicit_modifiers["Socketed Gems deal #% more Elemental Damage"]),
             Modifier(explicit_modifiers["# to Level of Socketed AoE Gems"], vmin=2),
             Modifier(pseudo_modifiers["+# total maximum Life"])
             ],
            filter_type="and"),
        base_type="Royal Burgonet"))

    meta_craft_beast = TradeObject(TypeQuery("Wild Bristle Matron"))

    chance_to_fail = three_mod * (1 - 0.377)  # 0.377 is the chance to hit +2 without a crafted mod

    finish_rf_helmet_strat = Strategy(
        StochasticList()
        .append(meta_craft_beast, 2.29)
        .append(CurrencyAmount(1, "veiled-chaos-orb"), 2.29)
        .append(CurrencyAmount(4, "chaos"), 2.29)  # craft cost of + number of zombies/skeletons
        .append(uncrafted_rf_helmet, 1 + (chance_to_fail * 2.29)),
        finished_rf_helmet)

    unfinished_diamond_flask = TradeObject(ModifierQuery(Modifier(explicit_modifiers["#% increased Critical Strike Chance during Flask Effect"], vmin=50),
                                                         Modifier(pseudo_modifiers["# Empty Prefix Modifiers"], vmin=1),
                                                         base_type="Diamond Flask"))

    finished_diamond_flask = TradeObject(ModifierQuery(Modifier(explicit_modifiers["#% increased Critical Strike Chance during Flask Effect"], vmin=50),
                                                       Modifier(enchant_modifiers["#% increased effect"], vmin=70),
                                                       Modifier(explicit_modifiers["#% increased effect"]),
                                                       base_type="Diamond Flask"), nth_result=2)

    finish_diamond_flask_strat = Strategy(StochasticList().append(unfinished_diamond_flask, 1)
                                          .append(CurrencyAmount(1, "enkindling-orb"), 26),
                                          StochasticList().append(finished_diamond_flask, 0.13514))


def parse_modifier_list():
    modifiers_list = [pseudo_modifiers, explicit_modifiers, implicit_modifiers, fractured_modifiers, enchant_modifiers, crafted_modifiers, veiled_modifiers, monster_modifiers, delve_modifiers, ultimatum_modifiers]
    f = open('id_to_modifier.json')
    data = json.load(f)
    for i, mod_group_i in enumerate(data['result']):
        for modifier_i in mod_group_i["entries"]:
            text = ""
            if isinstance(modifier_i["text"], list):
                for part_i in modifier_i["text"]:
                    text += part_i
            else:
                text = modifier_i["text"]
            modifiers_list[i][text] = modifier_i["id"]


init()
