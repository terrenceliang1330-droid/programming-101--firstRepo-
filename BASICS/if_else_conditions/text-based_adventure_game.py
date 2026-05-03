print("You are a brave knight on a quest to find the legendary Sword of Destiny. After days of adventuring, you find yourself in a path that leads to a crossroad. Do you go left towards the dark forest or right towards the mysterious cave?")
leftOrRight = input("Should you go to the left, or to the right?").lower()

if leftOrRight == "left":
    print("You venture into the dark forest. The trees are tall and the shadows are deep. Suddenly, you hear a growl. A wild wolf beast appears! Do you fight or run?")
    fightOrRun = input("Do you fight the beast or run away?").lower()

    if fightOrRun == "fight":

        headOrLegs = input("You draw your sword and engage in battle with the beast. Adrenaline pumps as you face the mighty creature but a choice must be made. Do you strike the beast's head or its legs?").lower()
        
        if headOrLegs == "head":
            print("You aim for the beast's head and strike with all your might. The beast howls in pain and falls to the ground, defeated. You have won the battle and continue on your quest for the Sword of Destiny!")

            keyOrBread = input("Suddenly, a door opens beneath you. You fall through a fortress of structures and land in a room. Inside are two items: a key and a piece of bread. Do you take the key or the bread?").lower()

            if keyOrBread == "key":
                print("You take the key and use it to open a door. Looking inside, someone pushes you and you fall into a pit of spikes. You should of known that life isn't that easy. Pathetic.")

            elif keyOrBread == "bread":
                print("You take the bread, but you aren't hungry.")
                EatOrPocket = input("Do you eat the bread or put it in your pocket?").lower()

                if EatOrPocket == "eat":
                    print("You eat the bread and die. It was poisoned. You weren't even hungry. Pathetic.")

                elif EatOrPocket == "pocket":
                    print("You put the bread in your pocket and continue on your quest. You don't trust any of the items in the room. You slice the room open with your sword and find the Sword of Destiny hidden inside. You awaken the power of the sword and fly out, becoming the greatest knight in history. Horray!")

                else:
                    print("Hmm? Think again. You get crushed by the falling ceiling in the process of indecision. Pathetic.")

            else:
                print("Hmm? Think again. You get crushed by the falling ceiling in the process of indecision. Pathetic.")

        elif headOrLegs == "legs":
            print("You slice the beast's legs off, but something goes wrong. The beast regenates its legs. You didn't know that it could regerate. You die in the hands of the beast due to lack of knowledge. Pathetic.")

        else:
            print("Hmm? Think again. You die in the process of indecision.")


    elif fightOrRun == "run": 
        print("You decide to run away from the beast, but no knight is a coward! You trip over a root and fall, allowing the beast to catch you. You die in the hands of a wolf. Pathetic.")


    else:
        print("Hmm? Think again. You die in the process of indecision.")





elif leftOrRight == "right":
    print("You venture into the mysterious cave. The air is damp and the darkness is suffocating. As you explore deeper, you see two glowing eyes staring at you; a dragon. Do you stab it in the eyes or try to sneak past it?")
    hideOrAttack = input("Do you hide from the dragon or attack it?").lower()

    if hideOrAttack == "hide":
        print("You try to desolve into the shadows and hide from the dragon, but it has a keen sense of smell. It detects your presence and breathes fire in your direction. You are burned to ashes in an instant. Coward.")

    elif hideOrAttack == "attack":
        print("You charge at the dragon's eyes and strike with your sword. The dragon howls in pain and falls to the ground, defeated. You continue on but the cave starts to collapse. You run as fast as you can, but you come across a fork in the path. Do you go left or right?")
        leftOrRight2 = input("Should you go to the left, or to the right?").lower()

        if leftOrRight2 == "left":
            print("You take the left path and find a hidden chamber. Inside, you discover that it is a dead end. You turn back but the cave has collapsed behind you. You are trapped and eventually die of starvation. Pathetic.")

        elif leftOrRight2 == "right":
            print("You take the right path and find an opening that leads you outside. You have escaped the collapsing cave and continue on your quest for the Sword of Destiny!")
            ignoreOrTalkWitch = input("As you continue on, you come across a witch. Do you ignore her or talk to her?").lower()

            if ignoreOrTalkWitch == "ignore":
                print("You ignore the witch and continue on your quest. However, the witch is offended by your rudeness and casts a spell on you, but before she can finish the spell, you draw your sword and stab her in the heart. The witch dies and you continue on your quest. You then walk upon a rock with the Sword of Destiny on it. You pick up the sword and awaken its power, becoming the greatest knight in history. Horray!")

            elif ignoreOrTalkWitch == "talk":
              print("You talk to the witch and she seems friendly. She offers you help but she then throws a potion of burning acid at you. You die in agony. Pathetic.")

            else:
                print("Hmm? Think again. The witch catches you off guard and curses you, causing you to die in the process of indecision. Pathetic.")

        else:
            print("Hmm? Think again. The cave collapses on you and you die. Pathetic.")
    else:
        print("Hmm? Think again. You die in the process of indecision.")




else:
    print("Hmm? Not a valid choice. You get cursed and die by a thundering lightning strike. An unheroic end to a pathetic adventure.")