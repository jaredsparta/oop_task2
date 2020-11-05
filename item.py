class Item:
    # This class is the base class for any order found on a menu
    def __init__(self, name, price):
        self.name = name
        self.price = price

    # Defines what happens when cast as string
    def __str__(self):
        return f"{self.name} for £{self.price}"
