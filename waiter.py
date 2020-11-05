
class Waiter(Menu):
    def __init__(self, menu, name = "Waiter"):
        self.name = name
        self.menu = menu
        self.orders = []

    def list_items(self):
        print("We are currently offering the following items:")
        self.menu.list_menu()


    def add_order(self, item, number):
        self.orders.append(item)
        item.ordered(number)
        

    def check_orders(self):
        for order in self.orders:
            print(order)
