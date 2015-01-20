import datetime

class Personality:
    def __init__(self):
        self.properties = {"name": "Martingale",
                           "version": 0.01,
                           "mirror_vision": False,
                           "birthday": datetime.datetime.now(),
                           "announce_hour": True,
                           "humor": 5}

    def get_property(self, prop):
        return self.properties[prop]

    def set_property(self, prop, value):
        self.properties[prop] = value

    def get_birthday(self):
        day = self.properties['birthday'].strftime('%A')
        month = self.properties['birthday'].strftime('%B')
        date = self.properties['birthday'].strftime('%d')
        year = self.properties['birthday'].strftime('%Y')
        return day + ', ' + month + ' ' + date + ', ' + year 


    def get_about_string(self, extended = False):
        if extended:
            info = []
            info.append("Hello, my name is " + self.properties['name'])
            info.append("I am an artificial intelligence system.")
            info.append("Currently, I am running version " + str(self.properties['version'] + " of Omni."))
            info.append("I was created on " + self.get_birthday())
            return info
        else:
            return ["My name is " + self.properties['name']]

        

