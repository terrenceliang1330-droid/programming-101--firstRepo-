print("You are a brave knight on a quest to find the legendary Sword of Destiny. After days of adventuring, you find yourself in a path that leads to a crossroad. Do you go left towards the dark forest or right towards the mysterious cave?")
x = input("Should you go to the left, or to the right?")

if x == "left" or x == "Left":
    print("You venture into the dark forest. The trees are tall and the shadows are deep. Suddenly, you hear a growl. A wild wolf beast appears! Do you fight or run?")
    y = input("Do you fight the beast or run away?")
    if y == "fight" or y == "Fight":
        print("You draw your sword and engage in battle with the beast. Adrenaline pumps as you face the mighty creature. After a fierce fight, you manage to defeat it and continue on your quest.")
    elif y == "run" or y == "Run":
        print("You decide to run away from the beast, but no knight is a coward! You trip over a root and fall, allowing the beast to catch you. You die in the hands of a wolf. Pathetic.")
    else:
        print("Hmm? Think again. You die in the process of indecision.")
        