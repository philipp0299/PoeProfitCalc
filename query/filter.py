class Filter:
    def __init__(self, modifiers=None, filter_type="and", filter_value_min=None, filter_value_max=None):
        if type(modifiers) is not list and type(modifiers) is not tuple:
            self.modifier_json = [modifiers.to_json()]
        else:
            self.modifier_json = list(map(lambda mod: mod.to_json(), modifiers))
        self.filter_type = filter_type
        self.filter_value_min = filter_value_min
        self.filter_value_max = filter_value_max
        self.modifiers = modifiers

    def to_json(self):
        return {
            "type": self.filter_type,
            "filters": self.modifier_json,
            "disabled": False,
            "value": {
                "min": self.filter_value_min,
                "max": self.filter_value_max
            }
        }

    def __str__(self):
        if len(self.modifiers) == 1 and self.filter_type == "and":
            return str(self.modifiers[0])
        if self.filter_type == "and":
            return " and ".join(str(s) for s in self.modifiers)
        if self.filter_type == "count" and self.filter_value_min == 1 and self.filter_value_max is None:
            return " or ".join(str(s) for s in self.modifiers)
        else:
            return self.filter_type + "(" + str(self.filter_value_min) + ", " + \
                str(self.filter_value_max) + ")" + "{" + ", ".join(str(s) for s in self.modifiers) + "}"
