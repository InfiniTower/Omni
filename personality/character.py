import datetime

class Personality:
    def __init__(self):
        self.properties = {"name": "Omni",
                           "birthday": datetime.datetime.now(),
                           "announce_hour": True,
                           "humor": 5}

    def get_property(self, prop):
        return self.properties[prop]

    def set_property(self, prop, value):
        self.properties[prop] = value
