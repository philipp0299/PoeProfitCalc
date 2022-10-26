class Modifier:
    def __init__(self, modifier_id, vmin=None, vmax=None):
        self.modifier_id = modifier_id
        self.vmin = vmin
        self.vmax = vmax

    def get_modifier_json(self):
        return {
            "id": self.modifier_id,
            "disabled": False,
            "value": {
                "min": self.vmin,
                "max": self.vmax
            }
        }
