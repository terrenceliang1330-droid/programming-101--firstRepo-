achievments = {"monster slayer", "treasure hunter", "explorer"}

print ("Welcome to the Achievment Tracker!")
print (f"Your current achievments: {', '.join(achievments)}")

while True: 
    print("Command Options: 'add' to add an achievment, 'list' to list all achievments, 'quit' to exit.")
    action = input("What would you like to do? ").lower().strip()

    if action == "quit":
        print("Exiting Achievment Tracker. Goodbye!")
        break

    elif action == "list":
        print(f"Your achievments: {', '.join(achievments)}")

    elif action == "add":
        new_achievment = input("What achievment would you like to add? ").lower().strip()
        if new_achievment in achievments:
            print(f"You already have the '{new_achievment}' achievment.")
        else:
            achievments.add(new_achievment)
            print(f"'{new_achievment}' has been added to your achievments!")

    else:
        print("Invalid command. Please choose 'add', 'list', or 'quit'.")