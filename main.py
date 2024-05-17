from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True
coffeeMake = CoffeeMaker()
menu = Menu()
moneyMachine = MoneyMachine()
while is_on:

    order = input(f"What would you like? {menu.get_items()}: ")
    if order == "off":
        is_on = False
    elif order == "report":
        coffeeMake.report()
        moneyMachine.report()
    else:
        drink = menu.find_drink(order)
        if coffeeMake.is_resource_sufficient(drink) and moneyMachine.make_payment(drink.cost):
            coffeeMake.make_coffee(drink)

