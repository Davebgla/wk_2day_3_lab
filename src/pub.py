class Pub:
    def __init__(self, name, till, drink):
        self.name = name
        self.till = till
        self.drink = drink

    def increase_till(self, amount):
        self.till += amount