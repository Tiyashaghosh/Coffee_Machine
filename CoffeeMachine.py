from Menu_Resouces import MENU, resources , earnings

QUARTERS = 0.25
DIMES = 0.10
PENNIES = 0.01
NICKEL = 0.05

def report():
    return f"Water: {resources["water"]}ml\nMilk: {resources["milk"]}ml\nCoffee: {resources["coffee"]}g\nMoney: ${earnings["money"]}"

def check_resources(drink):
    if MENU[drink]["ingredients"]["water"] > resources["water"]:
        print("Sorry there is not enough water.")
    elif drink != "espresso" and MENU[drink]["ingredients"]["milk"] > resources["milk"]:
        print("Sorry there is not enough milk.")
    elif MENU[drink]["ingredients"]["coffee"] > resources["coffee"]:
        print("Sorry there is not enough coffee.")
    else:
        payment(drink)

def payment(drink):
    print("Insert coins: ")
    quarters = float(input("Quarters: "))
    dimes = float(input("Dimes: "))
    pennies = float(input("Pennies: "))
    nickel = float(input("Nickel: "))

    amt_paid = (quarters * QUARTERS) + (dimes * DIMES) + (pennies * PENNIES) + (nickel * NICKEL)
    if amt_paid < MENU[drink]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
    else:
        earnings["money"] += MENU[drink]["cost"]
        change = round(amt_paid - MENU[drink]["cost"],2)
        if change != 0:
            print(f"Here is ${change} dollars in change")
    update_resources(drink)

def update_resources(drink):
    resources["water"] -= MENU[drink]["ingredients"]["water"]
    if drink != "espresso":
        resources["milk"] -= MENU[drink]["ingredients"]["milk"]
    resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]

    print(f"Here is your {drink}☕.Enjoy!")


machine_on = True

while machine_on:
    prompt = input("What would you like?(espresso/latte/cappuccino): ").lower()
    if prompt == "off":
        machine_on = False
    elif prompt == "report":
        print(report())
    elif prompt in MENU:
        check_resources(prompt)
    else:
        print("Please choose from the menu.")