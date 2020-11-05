from waiter import Waiter
from item import Item
from menu import Menu

# Creating a menu
# Create a waiter with a menu and add the items
Jared = Waiter("Jared")

Jared.menu.add_item("Pasta", 10)
Jared.menu.add_item("Burger", 12)
Jared.menu.add_item("Smoothie", 5)
Jared.menu.add_item("Salad", 7)
Jared.menu.add_item("Pizza", 15)
Jared.menu.add_item("Large Pizza", 21)
Jared.menu.add_item("Soup of the Day", 8)
Jared.menu.add_item("Falafel Wrap", 11)
Jared.menu.add_item("Curry", 13)
Jared.menu.add_item("Fried Rice", 6)
Jared.menu.add_item("Chips", 3)

print(f"\n      Hi there, I'm {Jared.name}. Can I take your order? ")

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
    # Checks if what you type is in the menu
    # If it's not, then you will go back to the start of the loop
    # Otherwise, your order will be noted down in the orders attribute
    if choice == "2":
        order = input("\nChoose an item on the menu please: ")
        if order.title() in Jared.menu.dictionary:
            Jared.add_order(Jared.menu.dictionary[order.title()])
            print(f"You have ordered {order.title()}")
        else:
            print("Sorry, we don't have that")
            continue
    
    # Checks the orders you've made and how much it costs
    if choice == "3":
        print("\nYou have ordered the following: ")
        Jared.check_orders()
        print(f"Altogether it costs £{Jared.cost()}")
        

    # Exits the while loop and program finishes
    if choice == "4":
        print("\nThanks for ordering with us! \nYour food will be ready shortly :)")
        break
    