money = 0

stock = {
    "sword": 10,
    "shield": 5,
    "john": 2,
    "bob": 3
}

inventory = {
    "sword": 100,
    "shield": 150, 
    "john": 5,
    "bob": 5
}

def buy_item(item):
    global money
    
    cost = inventory[item]

    money += cost
    stock[item] -= 1

    print(f"A {item} was bought for {cost} coins. You now have {money} coins and there are {stock[item]} {item}s left in stock.")

print("Welcome to the store!")

while True:
    print("Here are the items available for purchase:")
    for item, cost in inventory.items():
        print(f"{item}: {cost} coins")

    choice = input("What would you like to buy? (type 'exit' to leave) ").lower()

    if choice == "exit":
        print("Thanks for visiting the store! Goodbye!")
        break
    elif choice in inventory:
        if stock[choice] > 0:
            buy_item(choice)
        else:
            print(f"Sorry, {choice} is out of stock.")
    else:
        print("Sorry, we don't have that item in stock.")