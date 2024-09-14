from tabnanny import check

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

resources["money"] = 0

# TODO: 1. Print Report
def make_coffee(choice):
    for r in resources:
        if r in MENU[choice]["ingredients"]:
            resources[r] -= MENU[choice]["ingredients"][r]
    resources["money"] += MENU[choice]["cost"]
    print(f"Here's Your {choice}. Enjoy!")

def calculate_total_coins(quarters, nickels, dimes, pennies):
    return (quarters*.25) + (dimes*.10) + (nickels*.05) + (pennies*.01)

def calculate_balance(total, choice):
    bal = round((total-MENU[choice]["cost"]),2)
    if bal > 0:
        print(f"Here is ${bal} in change")
        return True
    else:
        print("Not Enough Money. Money refunded")
        return False

def check_enough_resource(choice):
    resource = ["milk", "water", "coffee"]
    for r in resource:
        if (r in MENU[choice]["ingredients"]) and (resources[r] - MENU[choice]["ingredients"][r]) < 0:
            print(f"Not enough {r}")
            return False
    return True

def coin_insert(choice):
    print("Please insert coins.")
    quarter_count = int(input("how many quarters?: "))
    dime_count = int(input("how many dimes?: "))
    nickel_count = int(input("how many nickels?: "))
    penny_count = int(input("how many pennies?: "))
    total = calculate_total_coins(quarter_count, dime_count, nickel_count, penny_count)
    return calculate_balance(total,choice)



do_continue = True
while do_continue:
    selection = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if selection == "report":
        for res in resources:
            print(f"{res}: {resources[res]}")
    elif check_enough_resource(selection):
        if coin_insert(selection):
            make_coffee(selection)
        else:
            exit()
    else:
        exit()
