from menu import Menu

class Waiter(Menu):
    def __init__(self, name = "Waiter"):
        menu = Menu()
        self.name = name
        self.menu = menu
        self.orders = []

    # Lists the items in the menu
    def list_items(self):
        print("\nWe are currently offering the following items:")
        self.menu.list_menu()

    # Adds the order to the list
    def add_order(self, item):
        self.orders.append(item)
        
    # Gives the list of orders
    def check_orders(self):
        for order in self.orders:
            print(order)
