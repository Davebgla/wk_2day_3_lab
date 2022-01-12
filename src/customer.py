class Customer:
    def __init__(self, name, wallet, age, drunkenness):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunkenness = drunkenness
        
    def pay_for_drink(self, price):
        self.wallet -= price

    def check_age(self, age):
        if age >= 18:
            return True
        else:
            return False

    def increase_drunkenness(self, level):
        self.drunkenness += level
        