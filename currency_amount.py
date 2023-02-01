import requests
import json


class CurrencyAmount:
    def __init__(self, amount, curr_type):
        self.amount = amount
        self.type = curr_type
        self.display_name = name_to_display_name(self.type)

    def __str__(self):
        return str(self.amount) + " " + self.type

    def __add__(self, other):
        other_amount = other.convert_to(self.type)
        return CurrencyAmount(self.amount + other_amount, self.type)

    def __sub__(self, other):
        other_amount = other.convert_to(self.type)
        return CurrencyAmount(self.amount - other_amount, self.type)

    def __mul__(self, other):
        return CurrencyAmount(self.amount * other, self.type)

    def __lt__(self, other):
        other_amount = other.convert_to(self.type)
        return self.amount < other_amount

    def convert_to(self, target):
        chaos_equiv_self = chaos_equivalance_of_name(self.type)
        chaos_equiv_target = chaos_equivalance_of_name(target)
        return self.amount * chaos_equiv_self / chaos_equiv_target

    def fetch_price(self):
        return self

# TODO Add manual override for divine price

def display_name_to_name(name):
    for currency in poe_ninja_ids:
        if currency["name"] == name:
            return currency["tradeId"]


def name_to_display_name(name):
    for currency in poe_ninja_ids:
        if 'tradeId' in currency and currency["tradeId"] == name:
            return currency["name"]


def id_to_name(id):
    for currency in poe_ninja_ids:
        if currency["id"] == id:
            return currency["tradeId"]


def name_to_id(name):
    for currency in poe_ninja_ids:
        if 'tradeId' in currency and currency["tradeId"] == name:
            return currency["id"]


def chaos_equivalance_of_name(name):
    if name == "chaos":
        return 1
    for line in poe_ninja_details:
        if line["currencyTypeName"] == name_to_display_name(name):
            return line["chaosEquivalent"]



headers = {'User-Agent': 'PoeProfitCalc (https://github.com/Dakri7/PoeProfitCalc.git)', 'accept': 'application/json'}
poe_ninja_endpoint = "https://poe.ninja/api/data/currencyoverview?league=Kalandra&type=Currency&language=en"
poe_ninja_response = requests.get(poe_ninja_endpoint, headers=headers)
poe_ninja_data = json.loads(poe_ninja_response.content)
poe_ninja_ids = poe_ninja_data["currencyDetails"]
poe_ninja_details = poe_ninja_data["lines"]
print("Loaded poe.ninja currency data")

