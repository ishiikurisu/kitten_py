class Cat:
    def __init__(self, pos, itens):
        self.pos = pos
        self.itens = itens
        self.moves = self.setup_moves()

    def setup_moves(self):
        moves = {}

        moves['up'] = "0 -1"
        moves['down'] = "0 1"
        moves['left'] = "-1 0"
        moves['right'] = "1 0"

        return moves

    def get_moves(self):
        return self.moves

    def get_pos(self):
        return "%d %d" % (self.pos[0], self.pos[1])

    def set_pos(self, x, y):
        # print self.get_pos()
        self.pos = [x, y]

    def add_item(self, item):
        self.itens.append(item)

    def write_itens(self):
        outlet = 'itens: '

        if len(self.itens) == 0:
            outlet += 'none'
        else:
            for it in self.itens:
                outlet += '%s' % (it.get_name())
            outlet.rstrip(' ')

        # print outlet
        return outlet
