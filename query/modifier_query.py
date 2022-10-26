class ModifierQuery:

    def __init__(self, *modifiers):
        if type(modifiers) is tuple:
            self.modifiers = list(map(lambda mod: mod.get_modifier_json(), modifiers))
        else:
            self.modifiers = modifiers

    def get_query_string(self):
        return {
            "query": {
                "stats": [
                    {
                        "type": "and",
                        "filters": self.modifiers,
                        "disabled": False
                    }
                ],
                "status": "online"
            }
        }
