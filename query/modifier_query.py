from query.filter import Filter


class ModifierQuery:

    def __init__(self, *modifiers, base_type=None):
        if type(modifiers) is tuple:
            if type(modifiers[0]) is Filter:
                self.filters = list(map(lambda mod: mod.to_json(), modifiers))
            else:
                self.filters = [Filter(modifiers).to_json()]
        else:
            if type(modifiers) is Filter:
                self.filters = [modifiers.to_json()]
            else:
                self.filters = [Filter(modifiers)]
        self.base_type = base_type
        self.modifiers = list(modifiers)

    def get_query_string(self):
        if self.base_type is None:
            return {
                "query": {
                    "stats": self.filters,
                    "status": "online"
                }
            }
        else:
            return {
                "query": {
                    "type": self.base_type,
                    "stats": self.filters,
                    "status": "online"
                }
            }

    def __str__(self):
        if len(self.modifiers) > 1:
            back = "["
            for i in range(len(self.modifiers)):
                if not i == 0:
                    back += ", "
                back += str(self.modifiers[i])
            back += "]"
            return back
        else:
            return str(self.modifiers[0])
