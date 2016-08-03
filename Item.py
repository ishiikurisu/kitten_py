import time

class Item:
    def __init__(self, t, n):
        self.update_time = t
        self.name = n
    def update(self, t):
        pass

class Food(Item):
    def __init__(self):
        self.name = 'food'
    def get_name(self):
        return self.name

class Box(Item):
    def __init__(self):
        self.name = 'box'
    def get_name(self):
        return self.name

class Toy(Item):
    def __init__(self):
        pass