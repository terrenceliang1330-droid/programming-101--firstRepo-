workout_session = {}

def add_exercise(name, reps):
    if name not in workout_session:
        workout_session[name] = []

    workout_session[name].append(reps)


def summarize_workout():
    print("Workout Summary:")

    for name, reps_list in workout_session.items():
        total_reps = sum(reps_list)
        print(f"Exercise:{name.title()}, Total Reps: {total_reps}")

print("Welcome to the Workout Tracker!")

active = True

while active:
    choice = input("Type 'add' to add an exercise, 'summarize' to see your workout, or 'quit' to exit: ").lower()

    if choice == 'add':
        add_exercise(name=input("Enter exercise name: "), reps=int(input("Enter number of reps: ")))

    elif choice == 'summarize':
        summarize_workout()

    elif choice == 'quit':
        active = False
        print("Exiting the Workout Tracker. Goodbye!")