from Loader import Loader
from Cat import *
import Item
import Place
import time

class Level:
    path = str()
    description = [["cat", "food"], ["floor", "bowl"]]
    conditions = {"food": "0 1"}
    
    #########
    # SETUP #
    #########
    def __init__(self, path):
        loader = Loader()

        self.path = path
        self.right_place = False
        self.description = loader.load(self.path, "leveldata")
        self.colours = loader.load(self.path, "entity_colours")
        self.song = loader.compose(self.path, "music")
        self.cat = self.set_cat()

    def get_song_name(self):
        return self.song

    def get_cat(self):
        return self.cat
    def set_cat(self):
        for it in self.description:
            if it[0] == 'cat': return it[2]
        else:
            return None
    def get_cat_i(self):
        for i, it in enumerate(self.description):
            if it[0] == 'cat': return i
        else:
            return -1

    def get_dimensions(self):
        return map(int, self.description[0])

    def get_data(self):
        [x, y] = self.description[0]
        data = self.new_board(x, y)

        for i in xrange(1, len(self.description)):
            item = self.description[i]
            [x, y] = item[1]
            data[x][y] = item[0]

        return data

    def __str__(self):
        return str(self.get_data())

    def new_board(self, x, y):
        board = []

        for i in xrange(y):
            line = []
            for j in xrange(x):
                line.append("floor")
            board.append(line)

        return board

    ########
    # DRAW #
    ########
    def item_at(self, x, y):
        for i, it in enumerate(self.description):
            if [x, y] == it[1]: return i
    def within_constrains(self, x, y):
        j, i = self.description[0]
        if x < i and x >= 0 and y < j and y >= 0:
            return True
        else:
            return False

    def move_cat(self, action):
        cat = self.get_cat()
        board = self.get_data()
        moves = cat.get_moves()
        cat.write_itens()
        x, y = map(int, cat.get_pos().split(' '))
        dx, dy = map(int, moves[action].split(' '))
        x, y = x + dx, y + dy

        if not self.within_constrains(x, y):
            raise StandardError

        if board[x][y] == 'food':
            i = self.item_at(x, y)
            it = self.description.pop(i)
            cat.add_item(it[2])
            board = self.get_data()

        if board[x][y] == 'bowl':
            self.right_place = True
        else:
            self.right_place = False

        if board[x][y] == 'box' and board[x+dx][y+dy] == 'floor':
            shit = self.description[self.item_at(x, y)]
            shit[1] = [x+dx, y+dy]
            board = self.get_data()

        if board[x][y] == 'floor':
            cat = self.description[self.get_cat_i()]
            cat[1] = [x, y]
            cat[2].set_pos(x, y)

    def update(self):
        data = self.description

        for it in data:
            try: it.update()
            except: pass

    def get_colour(self, ent):
        return self.colours[ent]

    def shit(self):
        pass

    def can_end(self):
        for it in self.description:
            if it[0] == 'food': return False
        else:
            return True

    def end(self):
        return (self.can_end() and self.right_place)
