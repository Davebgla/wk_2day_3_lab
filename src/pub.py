class Pub:
    def __init__(self, name, till, drinks):
        self.name = name
        self.till = till
        self.drinks = drinks

    def increase_till(self, amount):
        self.till += amount

    def breathalise_customer(self, alcohol_intake):
        if alcohol_intake >= 16:
            return "OUT!"
        else:
            return "One more!"