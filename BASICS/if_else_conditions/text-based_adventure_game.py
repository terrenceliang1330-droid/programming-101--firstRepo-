print("You are a brave knight on a quest to find the legendary Sword of Destiny. After days of adventuring, you find yourself in a path that leads to a crossroad. Do you go left towards the dark forest or right towards the mysterious cave?")
leftOrRight = input("Should you go to the left, or to the right?").lower()

if leftOrRight == "left":
    print("You venture into the dark forest. The trees are tall and the shadows are deep. Suddenly, you hear a growl. A wild wolf beast appears! Do you fight or run?")
    fightOrRun = input("Do you fight the beast or run away?").lower()

    if fightOrRun == "fight":

        headOrLegs = input("You draw your sword and engage in battle with the beast. Adrenaline pumps as you face the mighty creature but a choice must be made. Do you strike the beast's head or its legs?").lower()
        
        if headOrLegs == "head":
            print("You aim for the beast's head and strike with all your might. The beast howls in pain and falls to the ground, defeated. You have won the battle and continue on your quest for the Sword of Destiny!")


        elif headOrLegs == "legs":
            print("You slice the beast's legs off, but something goes wrong. The beast regenates its legs. You didn't know that it could regerate. You die in the hands of the beast due to lack of knowledge. Pathetic.")


    elif fightOrRun == "run": 
        print("You decide to run away from the beast, but no knight is a coward! You trip over a root and fall, allowing the beast to catch you. You die in the hands of a wolf. Pathetic.")


    else:
        print("Hmm? Think again. You die in the process of indecision.")



