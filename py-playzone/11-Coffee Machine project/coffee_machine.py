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

profits = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def availability(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coins(customer_order):
    global profits
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: "))   * 0.10
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    change = round(total - MENU[customer_order]["cost"], 2)
    if change >= 0:
        profits += total - change
        print(f"Here is ${change} in change.")
    else:
        print("Sorry that's not enough money. Money refunded.")

def make_coffee(order_ingredients,drink):
        for item in order_ingredients:
            resources[item]-=order_ingredients[item]
        print(f"Here is your {drink} ☕️. Enjoy!")

is_on=True
while is_on:
    order=input("What would you like? (espresso/latte/cappuccino): ")
    if order=='off':
        print("Shutting down.....")
        is_on=False


    elif order=="report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profits}")

    else:
        ordered_ingredients = MENU[order]
        if availability(ordered_ingredients["ingredients"]):
            process_coins(order)
            make_coffee(ordered_ingredients["ingredients"],order)






