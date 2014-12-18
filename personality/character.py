class Personality:
    def __init__(self):
        self.properties = {"name": "Omni"}

    def get_property(self, prop):
        return self.properties[prop]

    def set_property(self, prop, value):
        self.properties[prop] = value
