from waiter import Waiter
from item import Item
from menu import Menu

# Creating a menu
# First we must create some items to sell:
pasta = Item("Pasta", 10, 50)
burger = Item("Burger", 8, 100)
smoothie = Item("Smoothie", 5, 100)
salad = Item("Salad", 7, 100)

# Creating a Waiter instance
Jared = Waiter(menu, "Jared")

print(f"Hi there, I'm {Jared.name}. Can I take your order? ")
while True:
    choice = input("""
                    1. I can show you our menu or
                    2. You can order something or
                    3. I can tell you your order
                    4. Or are you finished with ordering?
                     ->  """)

    if choice == "1":
        Jared.list_items()
        
    
    if choice == "2":
        print(Jared.self.menu)
        
    
    