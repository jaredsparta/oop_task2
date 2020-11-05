from waiter import Waiter
from item import Item
from menu import Menu

# Creating a menu
# Create a waiter with a menu and add the items
Jared = Waiter("Jared")

Jared.menu.add_item("Pasta", 10)
Jared.menu.add_item("Burger", 8)
Jared.menu.add_item("Smoothie", 5)
Jared.menu.add_item("Salad", 7)


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
        order = input("\nChoose an item on the menu please: ")
        if order.title() in Jared.menu.dictionary:
            Jared.add_order(Jared.menu.dictionary[order.title()])
        else:
            print("Sorry, we don't have that")
            continue
    

    if choice == "3":
        Jared.check_orders()


    if choice == "4":
        break
    