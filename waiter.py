# This class creates a Waiter with a name
# Each waiter has an associated menu they can serve food from
# They store the orders the user makes also
from menu import Menu

class Waiter(Menu):
    def __init__(self, name = "Waiter"):
        # I initialise a menu object to serve as the waiter's menu
        menu = Menu()
        self.name = name
        self.menu = menu
        self.orders = []

    # Lists the items in the menu
    # Uses a Menu method to achieve it
    def list_items(self):
        print("\nWe are currently offering the following items:")
        self.menu.list_menu()

    # Adds the order to the list of orders
    def add_order(self, item):
        self.orders.append(item)
        
    # Repeats the orders that the user has asked for
    def check_orders(self):
        for order in self.orders:
            print(order)

    # Returns the cost of the orders
    def cost(self):
        cost = 0
        for order in self.orders:
            cost += order.price
        return cost
