from menu import Menu

class Waiter(Menu):
    def __init__(self, name = "Waiter"):
        menu = Menu()
        self.name = name
        self.menu = menu
        self.orders = []

    def list_items(self):
        print("\nWe are currently offering the following items:")
        self.menu.list_menu()


    def add_order(self, item):
        self.orders.append(item)
        
        

    def check_orders(self):
        for order in self.orders:
            print(order)
