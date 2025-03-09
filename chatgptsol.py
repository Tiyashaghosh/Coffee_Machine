from Menu_Resouces import MENU, resources, earnings

QUARTERS = 0.25
DIMES = 0.10
PENNIES = 0.01
NICKEL = 0.05

def report():
    return (f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\n"
            f"Coffee: {resources['coffee']}g\nMoney: ${earnings['money']}")

def check_resources(drink):
    for item, amount in MENU[drink]["ingredients"].items():
        if resources[item] < amount:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True

def process_payment(drink):
    print("Insert coins: ")
    try:
        quarters = float(input("Quarters: "))
        dimes = float(input("Dimes: "))
        pennies = float(input("Pennies: "))
        nickel = float(input("Nickel: "))
    except ValueError:
        print("Please enter valid numbers for coins.")
        return False

    amt_paid = (quarters * QUARTERS) + (dimes * DIMES) + (pennies * PENNIES) + (nickel * NICKEL)
    if amt_paid < MENU[drink]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        earnings["money"] += MENU[drink]["cost"]
        change = round(amt_paid - MENU[drink]["cost"], 2)
        if change > 0:
            print(f"Here is ${change} dollars in change.")
        return True

def update_resources(drink):
    for item, amount in MENU[drink]["ingredients"].items():
        resources[item] -= amount
    print(f"Here is your {drink} ☕. Enjoy!")

machine_on = True

while machine_on:
    prompt = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if prompt == "off":
        machine_on = False
    elif prompt == "report":
        print(report())
    elif prompt in MENU:
        if check_resources(prompt):
            if process_payment(prompt):
                update_resources(prompt)
    else:
        print("Please choose from the menu.")
