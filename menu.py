from item import Item

class Menu(Item):
    def __init__(self):
        self.menu = []
        self.dictionary = {}

    # Adds an item to the menu
    def add_item(self, name, price):
        item_to_add = Item(name, price)
        self.menu.append(item_to_add)
        self.dictionary[item_to_add.name] = item_to_add

    # Lists the items on the menu
    def list_menu(self):
        for item in self.menu:
            print(item)
