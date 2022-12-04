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
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resource_sufficient (order_ingredients ):
    "Sprawdza dostępne zasoby w maszynie do zrobienia kawy. "
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item] :
            print(f"sorry, that's not enough {item}. ")
            return False
    return True

def process_coins():
    """Zwraca wartośc wszystkich wrzuconych monet"""
    print("Please iinsert coins.")
    total = int(input("How many quaters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.10
    total += int(input ("How manny nickles? ")) * 0.05
    total += int(input("How many pennies?")) * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    """Zwraca prawde kiedy płatnosc jest zaakceptowana i falsz kiedy jest zbyt mało pieniedzy."""
    if money_received >= drink_cost:
        global profit
        profit += drink_cost
        change = round(money_received - drink_cost , 2)
        print(f"That's your change ${change}")
        return True
    else:
        print("Sorry, that's not enough money.")
        return False

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕ ")

want_coffee = True

while want_coffee:
    choice = input("What would you like?(espresso/latte/cappucino): ").lower()
    if choice == "off":
        want_coffee = False
    elif choice == "report":
        print(f"Water:{resources['water'] } ml ")
        print(f"Milk: {resources['milk'] } ml ")
        print(f"Coffee: {resources['coffee'] } ml ")
        print(f"Money: ${profit}  ")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(choice, drink['ingredients'])



