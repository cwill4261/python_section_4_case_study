from lesson_examples import load_shots, clean_shots, prepare_shots


def main():
    shots = prepare_shots(clean_shots(load_shots()))

    # TODO 1: Change this to another season in the dataset.
    season = "2015-2016"

    season_shots = shots.loc[shots["season"] == season]

    # TODO 2: Use .loc to keep only three-point attempts.
    # Start with season_shots.loc[...].
    # Inside the brackets, write a condition that checks whether
    # season_shots["shot_type"] equals "3PT Field Goal".
    # Use == to compare the values.
    three_point_shots = season_shots  # Replace this line.

    attempts = len(three_point_shots)
    makes = three_point_shots["shot_made_flag"].sum()

    if attempts == 0:
        print("No matching attempts. Check your season and filter.")
        return

    # TODO 3: Replace None with the shooting-percentage calculation.
    # Divide makes by attempts, then multiply by 100.
    # Use the variables already calculated above.
    shooting_pct = None

    print(f"Season: {season}")

    if shooting_pct is None:
        print(f"Selected attempts: {attempts:,}")
        print(f"Selected makes: {makes:,}")
        print("Complete TODOs 2 and 3 to calculate three-point accuracy.")
    else:
        print("Shot selection: Regulation-time three-pointers")
        print(f"Three-point attempts: {attempts:,}")
        print(f"Three-pointers made: {makes:,}")
        print(f"Three-point shooting percentage: {shooting_pct:.2f}%")


if __name__ == "__main__":
    main()