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
profit=0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def order_sufficicent(order_ingredients):
    for item in order_ingredients:
        if resources[item]<=order_ingredients[item]:
            print(f"Sorry there is not enough {item} .")
            return False
    return True
def process_coin():
    print("Please insert a coin .")
    total=int(input("how many quaters?:")) * 0.25
    total += int(input("how many dimes?:")) * 0.1
    total +=int(input("how many nickels?:")) * 0.05
    total  += int(input("how many pennies?:")) * 0.01

def is_transaction_successful(money_recieved , drink_cost):
    if money_recieved>=drink_cost:
        change = round(money_recieved-drink_cost,2)
        print(f"here is ${change} in change.")
        global  profit
        profit+=drink_cost
        return True
    else:
        print("sorry thats not enough money , money refounded .")
        return False
def to_make_coffe(drink_name,order_incredient):
    for item in order_incredient:
        resources[item]-=order_incredient
    print(f"here's your drink name {drink_name}")

is_on=True
while True:
    choice=input("What do you like?(espresso/latte/cappucion): ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if order_sufficicent(drink['ingredients']):
            payment = process_coin()
            if is_transaction_successful(payment,drink['cost']):
                to_make_coffe()
















