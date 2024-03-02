#TODO 2: check the cost of the iteam
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
def print_resources():
    print(f"Resources:\nWater:{resources['water']}\nMilk:{resources['milk']}\nCoffee:{resources['coffee']}")
def check(resources,menu,item):
    f=True
    if resources["water"]<menu["water"]:
        f=False
    if  item!="espresso":
        if resources["milk"]<menu["milk"]:
            f=False
    if resources["coffee"]<menu["coffee"]:
        f=False
    return f
def item1(item):
    profit=0
    total=process_coins()
    if MENU[item]["cost"]<total:
        money=total-MENU[item]["cost"]
        print(f"You change is {round(money,2)}")
        print(f"Enjoy your {item} 😊😁👍")
        profit+=MENU[item]["cost"]
    menu=MENU[item]["ingredients"]
    if item=="espresso" or item=="latte" or item=="cappuccino":
        if check(resources,MENU[item]["ingredients"],item):
            resources["water"]-=menu["water"]
            if item != "espresso":
                resources["milk"]-=menu["milk"]
            resources["coffee"]-=menu["coffee"]
    elif item=="off":
        print_resources()
        print(f"Money:{profit}")

    else:
        global f
        print("There is not resources:")
        print_resources()
        f=False
        
def process_coins():
    print("Please insert the coins")
    total = int(input("how many quarters?:")) * 0.25
    total += int(input("how many dimes?:")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total
#TODO 1: print all the ingredients left when the user type report
print("Wellcome to Coffee Machine")
f=True
while True:
    print(f"Espresso:{MENU['espresso']['cost']}\nLatte:{MENU['latte']['cost']}\nCappuccino:{MENU['cappuccino']['cost']}")
    item=input("What would you like? (espresso/latte/cappuccino):\n")
    item1(item)



