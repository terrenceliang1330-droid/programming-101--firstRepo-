import random
import time
import os

colours = ["red", "blue", "green", "yellow"]

print("Welcome to the repeat after me game!")
print("I will show you a colour and you have to repeat it back to me. Just type out the colour and press enter, then type the next and so on.")

while True:

    sequence = []
    game_over = False

    print("Get ready...")
    time.sleep(1)

    while not game_over:

        new_colour = random.choice(colours)
        sequence.append(new_colour)

        print("Memorize this colour pattern")
        time.sleep(1)

        for color in sequence:
            print(color)
            time.sleep(0.5)

            os.system('cls' if os.name == 'nt' else 'clear')

            print("Now repeat the pattern back to me!")

            for correct_colour in sequence:
                player_guess = input("Enter the colour: ").strip().lower()

                if player_guess != correct_colour:
                    print("Wrong colour! Game over.")
                    game_over = True
                    break

        if not game_over:
            print("Correct! Get ready for the next round.")
            time.sleep(1)

    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again != "yes":
        print("Thanks for playing! Goodbye!")
        break