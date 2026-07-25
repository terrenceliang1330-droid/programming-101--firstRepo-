workout_session = {}

def add_exercise(name, reps):
    if name not in workout_session:
        workout_session[name] = []

    workout_session[name].append(reps)


def summarize_workout():
    print("Workout Summary:")

    for name, reps_list in workout_session.items():
        total_reps = sum(reps_list)
        print(f"Exercise:{name}, Total Reps: {total_reps}")

