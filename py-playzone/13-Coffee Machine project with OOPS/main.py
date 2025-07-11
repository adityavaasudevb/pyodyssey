from sympy import false

from menu import Menu,MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# we must create an object to use the attributes and methods associated with the class

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
is_on=True

while is_on:
    order = menu.get_items()
    choice = input(f"what would you like? ({order}) ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice) # it returns a menu item object thats why we can use drink.cost in the condition below
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)




