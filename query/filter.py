class Filter:
    def __init__(self, modifier_list=None, filter_type="and", filter_value_min=None, filter_value_max=None):
        self.modifier_list = list(map(lambda mod: mod.to_json(), modifier_list))
        self.filter_type = filter_type
        self.filter_value_min = filter_value_min
        self.filter_value_max = filter_value_max

    def to_json(self):
        return {
            "type": self.filter_type,
            "filters": self.modifier_list,
            "disabled": False,
            "value": {
                "min": self.filter_value_min,
                "max": self.filter_value_max
            }
        }