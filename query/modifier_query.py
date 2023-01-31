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

