class Timer:
    def __init__(self, time, ID):
        self.time = time
        self.ID = ID

    def increment(self):
        self.time -= 1
        if self.time == 0:
            return True
        else:
            return False

    def get_id(self):
        return self.ID


class TimeModule:
    def __init__(self):
        self.timers = []
        self.id_cnt = 0

    def add_timer(self, time):
        self.id_cnt += 1
        self.timers.append(Timer(time, self.id_cnt))
        return self.id_cnt

    def update(self):
        keep_time = []
        buzz = []
        for t in self.timers:
            if t.increment():
                buzz.append(t.get_id())
            else:
                keep_time.append(t)
        self.timers = keep_time
        return buzz

