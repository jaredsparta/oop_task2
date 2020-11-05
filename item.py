class Item:
    # This class is the base class for any order found on a menu
    def __init__(self, item_name, item_price, item_availability):
        self.item_name = item_name
        self.item_price = item_price
        self.item_availability = item_availability

    # There will only be a set number of times the order can be ordered
    # Realistically, this makes sense since ingredients are finite
    # This method will increment this logic
    def ordered(self, number_ordered):
        self.item_availability -= number_ordered
        pass

    def __str__(self):
        return f"{self.item_name} for £{self.item_price}"
