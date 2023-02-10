from query.filter import Filter


class ModifierQuery:

    def __init__(self, *modifiers, base_type=None, name=None):
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
        self.name = name
        self.modifiers = list(modifiers)

    def get_query_string(self):
        back = {
                "query": {
                    "stats": self.filters,
                    "status": "online"
                }
        }
        if self.base_type is not None:
            back["query"]["type"] = self.base_type
        if self.name is not None:
            back["query"]["name"] = self.name
        return back

    def __str__(self):
        if len(self.modifiers) > 1:
            back = ""
            if self.base_type is not None:
                back += self.base_type
            back += "["
            for i in range(len(self.modifiers)):
                if not i == 0:
                    back += ", "
                back += str(self.modifiers[i])
            back += "]"
            return back
        else:
            return str(self.modifiers[0])
