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

# This code will run until we insert 4 as a choice
while True:
    choice = input("""
                    1. Show menu
                    2. Order something
                    3. Show current order list
                    4. Finish with ordering
                     ->  """)

    # Lists the menu
    if choice == "1":
        Jared.list_items()

    # Allows you to order
    if choice == "2":
        order = input("\nChoose an item on the menu please: ")
        if order.title() in Jared.menu.dictionary:
            Jared.add_order(Jared.menu.dictionary[order.title()])
        else:
            print("Sorry, we don't have that")
            continue
    
    # Checks the orders you've mad
    if choice == "3":
        print("\nYou have ordered the following: ")
        Jared.check_orders()

    # Exits the while loop and program finishes
    if choice == "4":
        break
    