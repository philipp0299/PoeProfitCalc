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
