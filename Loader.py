from Level import *
from Cat import *
from Item import *
from Place import *
import os

class Loader:
    def __init__(self):
        if os.name == 'posix':
            self.sep = "/"
        else:
            self.sep = "\\"

    def get_images(self, level):
        inlet = level.colours
        outlet = []

        for it in inlet:
            outlet.append(path + it)

        return outlet

    def load(self, path, att):
        outlet = None
        path = path + self.sep + att + ".dsp"
        fp = open(path, "r")

        if outlet == 'leveldata':
            outlet = []
        else:
            outlet = {}

        for line in fp:
            inlet = line.rstrip()
            outlet = self.parse(inlet, outlet)

        fp.close()
        return outlet

    def parse(self, string, data):
        inlet = string.split(" ")
        g = globals()

        if inlet[0] == 'size':
            x = int(inlet[1])
            y = int(inlet[2])
            return [[y, x]]
        elif inlet[0] == 'init':
            x, y = map(int, [inlet[1], inlet[2]])
            cat = g['Cat']([x, y], [])
            data.append(['cat', [x, y], cat])
        elif inlet[0] == 'item':
            x, y = map(int, [inlet[2], inlet[3]])
            it = g[inlet[1].capitalize()]()
            data.append([inlet[1], [x, y], it])
        elif inlet[0] == 'place':
            x, y = map(int, [inlet[2], inlet[3]])
            data.append([inlet[1], [x, y]])
        elif inlet[0] == 'end':
            x, y = map(int, [inlet[1], inlet[2]])
            data.append(['bowl', [x, y]])
        else:
            data[inlet[0]] = inlet[1]

        return data

    def compose(self, path, name):
        return path + self.sep + name + '.mp3'

    def new_board(self, x, y):
        board = []

        for j in xrange(x):
            strip = []
            for i in xrange(y):
                strip.append("floor")
            board.append(strip)

        return board
