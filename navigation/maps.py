class Map:
    def __init__(self, resolution, sizex, sizey):
        self.res = resolution
        self.sizex = sizex
        self.sizey = sizey
        self.passability = np.zeros([sizex, sizey])

    def set_passage(self, pos, psg):
        self.passability[pos] = psg

    def get_passable(self, pos):
        return self.passability[pos]




