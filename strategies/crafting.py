from query.filter import Filter
from query.modifier_query import ModifierQuery
from query.modifier import Modifier
from trade_object import TradeObject
from strategy import Strategy
from object_lists.stochastic_list import StochasticList
from currency_amount import CurrencyAmount

finish_rf_helmet_strat = None


def init():
    global finish_rf_helmet_strat

    uncrafted_rf_helmet = TradeObject(ModifierQuery(
        Filter(
            [Modifier("explicit.stat_2680613507"), Modifier("explicit.stat_3835899275")], filter_type="and"),
        Filter(
            [Modifier("pseudo.pseudo_number_of_crafted_prefix_mods", vmin=1),
             Modifier("pseudo.pseudo_number_of_prefix_mods", vmax=2)], filter_type="count", filter_value_min=1),
        base_type="Eternal Burgonet"))

    finished_rf_helmet = TradeObject(ModifierQuery(
        Filter(
            [Modifier("explicit.stat_2680613507"),
             Modifier("explicit.stat_3835899275"),
             Modifier("explicit.stat_2551600084", vmin=2)], filter_type="and"),
        base_type="Eternal Burgonet"))

    finish_rf_helmet_strat = Strategy(
        StochasticList().append(CurrencyAmount(2, "divine"), 2.29)
        .append(CurrencyAmount(1, "veiled-chaos-orb"),2.29)
        .append(uncrafted_rf_helmet, 1),
        finished_rf_helmet)


init()
