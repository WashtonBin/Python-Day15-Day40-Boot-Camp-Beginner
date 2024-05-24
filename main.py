MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

#TODO 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
# a. Check the user’s input to decide what to do next.
# b. The prompt should show every time action has completed, e.g. once the drink is
# dispensed. The prompt should show again to serve the next customer.


"""prompt user coffee input"""
def prompt_user():
    prompt = input("What would you like? (espresso/latte/cappuccino): ").lower()
    return prompt

"""insert coins"""
def insert_coins():
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.1
    nickles = int(input("How many quarters?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01
    return quarters + dimes + nickles + pennies


"""prompt water """
def make_water(prompt_user, water):
    if water >= MENU[prompt_user]["ingredients"]["water"]:
        return water - MENU[prompt_user]["ingredients"]["water"]
    else:
        print("Sorry that's not enough water.")
        return water

"""prompt milk"""
def make_milk(prompt_user, milk):
    if milk >= MENU[prompt_user]["ingredients"]["milk"]:
        return milk - MENU[prompt_user]["ingredients"]["milk"]
    else:
        print("Sorry that's not enough milk.")
        return milk

"""prompt milk"""
def make_coffee(prompt_user, coffee):
    if coffee >= MENU[prompt_user]["ingredients"]["coffee"]:
        return coffee - MENU[prompt_user]["ingredients"]["coffee"]
    else:
        print("Sorry that's not enough coffee.")
        return coffee

def suffcient_resources(order_ingredient):
    for item in order_ingredient:
        if resources[item] > order_ingredient[item]:
            return False
    return True




"""execute coffee machine"""
def coffee_machine():
    #get initial values from dictionaries
    is_on = True
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    money = 0
    #turn coffee machine
    while is_on is True:
        prompt = prompt_user()
        if prompt == "report":
            print(f"Water: {water}ml")
            print(f"Milk: {milk}ml")
            print(f"Coffee: {coffee}g")
            print(f"Money: ${round(money, 2)}")
        elif prompt == "off":
            print("Coffee Machine is off.")
            is_on = False
        elif prompt == "latte" or prompt == "cappuccino":
            # check if water, coffee, and milk are out of service
            make_water(prompt, water)
            make_coffee(prompt, coffee)
            make_milk(prompt, milk)
            # check water, coffee, milk condition if not come back to the main menu
            if water >= MENU[prompt]["ingredients"]["water"] and coffee >= MENU[prompt]["ingredients"]["coffee"] and milk >= MENU[prompt]["ingredients"]["milk"]:
                print("Please insert coins")
                coins = insert_coins()
                if MENU[prompt]["cost"] <= coins:
                    # get values from make_method
                    water = make_water(prompt, water)
                    coffee = make_coffee(prompt, coffee)
                    milk = make_milk(prompt, milk)
                    # set money print 2 decimal place
                    money += round(MENU[prompt]["cost"], 2)

                    print(f"Here is ${round(coins - MENU[prompt]["cost"], 2)} in change.")
                    print("Here is your espresso 😀 Enjoy")
                else:
                    print(f"Sorry that's not enough money.${coins} refunded.")

        elif prompt == "espresso":
            make_water(prompt, water)
            make_coffee(prompt, coffee)
            # only check water and coffee
            if water >= MENU[prompt]["ingredients"]["water"] and coffee >= MENU[prompt]["ingredients"]["coffee"]:
                print("Please insert coins")
                coins = insert_coins()
                if MENU[prompt]["cost"] <= coins:
                    water = make_water(prompt, water)
                    coffee = make_coffee(prompt, coffee)
                    money += round(MENU[prompt]["cost"], 2)

                    print(f"Here is ${round(coins - MENU[prompt]["cost"], 2)} in change.")
                    print("Here is your espresso 😀 Enjoy")
                else:
                    print(f"Sorry that's not enough money.${coins} refunded.")
        else:
            print("The input is invalid.")

coffee_machine()



#TODO 2. Turn off the Coffee Machine by entering “off” to the prompt.
# a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off
# the machine. Your code should end execution when this happens.

#TODO 3. Print report.
# a. When the user enters “report” to the prompt, a report should be generated that shows
# the current resource values. e.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5

#TODO 4. Check resources sufficient?
# a. When the user chooses a drink, the program should check if there are enough
# resources to make that drink.
# b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
# not continue to make the drink but print: “Sorry there is not enough water.”
# c. The same should happen if another resource is depleted, e.g. milk or coffee.



#TODO 5. Process coins.
# a. If there are sufficient resources to make the drink selected, then the program should
# prompt the user to insert coins.
# b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
# c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
# pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52



#TODO 6. Check transaction successful?
# a. Check that the user has inserted enough money to purchase the drink they selected.
# E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
# program should say “Sorry that's not enough money. Money refunded.”.
# b. But if the user has inserted enough money, then the cost of the drink gets added to the
# machine as the profit and this will be reflected the next time “report” is triggered. E.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# c. If the user has inserted too much money, the machine should offer change.
# E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal
# places.



#TODO 7. Make Coffee.
# a. If the transaction is successful and there are enough resources to make the drink the
# user selected, then the ingredients to make the drink should be deducted from the
# coffee machine resources.
# E.g. report before purchasing latte:
# Water: 300ml
# Milk: 200ml
# Coffee: 100g
# Money: $0
# Report after purchasing latte:
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If
# latte was their choice of drink
