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
