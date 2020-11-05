from waiter import Waiter
from item import Item
from menu import Menu

# Creating a menu
# First we must create some items to sell:
pasta = Item("Pasta", 10, 50)

# Creating a Waiter instance
Jared = Waiter(menu, "Jared")

print(f"Hi there, I'm {Jared.name}. Can I take your order? ")
while True:
    