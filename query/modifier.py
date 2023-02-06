import json

class Modifier:
    def __init__(self, modifier_id, vmin=None, vmax=None, option=None):
        self.modifier_id = modifier_id
        self.vmin = vmin
        self.vmax = vmax
        self.option = option

    def to_json(self):
        if self.option is None:
            return {
                "id": self.modifier_id,
                "disabled": False,
                "value": {
                    "min": self.vmin,
                    "max": self.vmax
                }
            }
        else:
            return {
                "id": self.modifier_id,
                "disabled": False,
                "value": {
                    "option": self.option
                }
            }

    def __str__(self):
        if self.option is not None:
            return self.modifier_id + "[" + str(self.option) + "]"
        if self.vmin is None and self.vmax is None:
            return self.modifier_id
        if self.vmin is not None and self.vmax is not None:
            return str(self.vmin) + " < " + self.modifier_id + " < " + str(self.vmax)
        if self.vmin is not None:
            return self.modifier_id + " > " + str(self.vmin)
        if self.vmax is not None:
            return self.modifier_id + " < " + str(self.vmax)


_all_modifiers = {}


def parse_modifier_list():
    global _all_modifiers
    modifiers_types = ["pseudo", "explicit", "implicit", "fractured", "enchant", "crafted", "veiled", "monster", "delve", "ultimatum"]
    _all_modifiers = {mod_type: {} for mod_type in modifiers_types}
    f = open('id_to_modifier.json')
    data = json.load(f)
    for i, mod_group_i in enumerate(data['result']):
        mod_type = modifiers_types[i]
        for modifier_i in mod_group_i["entries"]:
            text = ""
            if isinstance(modifier_i["text"], list):
                for part_i in modifier_i["text"]:
                    text += part_i
            else:
                text = modifier_i["text"]
            _all_modifiers[mod_type][text] = modifier_i["id"]


def from_text(text, mod_type="explicit", *argv, **kwargs):
    return Modifier(_all_modifiers[mod_type][text], *argv, **kwargs)


parse_modifier_list()