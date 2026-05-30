bestiary = {
    "goblin": 15,
    "troll": 30,
    "dragon": 100,
    "unicorn": 50,
    "phoenix": 1000,
    "orc": 40,
    "giant": 80,
    "vampire": 60,
    "werewolf": 70,
    "zombie": 20,
    "skeleton": 10,
    "slime": 5
}

print ("WELCOME TO THE BESTIARY!")
print(f"Discovered monsters: {', '.join(bestiary.keys())}")

while True:
    monster_search = input("Which monster would you like to learn about? Type 'quit' to exit. Type 'list monsters' to see all monsters.").lower()

    if monster_search == "quit":
        print("Closing bestiary.")
        break


    elif monster_search == "list monsters":
        print(f"Discovered monsters: {', '.join(bestiary.keys())}")

    elif monster_search in bestiary:
        print(f"The {monster_search} has the health level of {bestiary[monster_search]}.")

    elif monster_search == "add monster":
        new_monster = input("What monster would you like to add?").lower()
        if new_monster in bestiary:
            print(f"The {new_monster} is already in the bestiary.")
        else:
            new_health = input(f"What is the health level of the {new_monster}?")
            if new_health.isdigit():
                bestiary[new_monster] = int(new_health)
                print(f"The {new_monster} has been added to the bestiary with a health level of {new_health}.")
            else:
                print("Health level must be a number. Please try again.")


    else:
        print(f"Sorry, the {monster_search} is not in the bestiary. Please check your spelling and try again.")

    