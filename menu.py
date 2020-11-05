from item import Item

class Menu(Item):
    def __init__(self):
        self.menu = []

    
    def add_item(self, name, price, availability):
        item_to_add = Item(name, price, availability)
        self.menu.append(item_to_add)


    def list_menu(self):
        for item in self.menu:
            print(item)
