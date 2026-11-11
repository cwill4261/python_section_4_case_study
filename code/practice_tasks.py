from lesson_examples import load_shots, clean_shots, prepare_shots


def main():
    shots = prepare_shots(clean_shots(load_shots()))

    # TODO 1: Change this to another season in the dataset.
    season = "2015-2016"

    season_shots = shots.loc[shots["season"] == season]

    # TODO 2: Filter season_shots to keep only three-point attempts.
    # Hint: the shot_type value is "3PT Field Goal".
    three_point_shots = season_shots  # Replace this line.

    attempts = len(three_point_shots)
    makes = three_point_shots["shot_made_flag"].sum()

    if attempts == 0:
        print("No matching attempts. Check your season and filter.")
        return

    # TODO 3: Calculate shooting percentage.
    # Formula: makes divided by attempts, multiplied by 100.
    shooting_pct = None  # Replace None with your calculation.

    print(f"Season: {season}")
    print(f"Selected attempts: {attempts:,}")
    print(f"Selected makes: {makes:,}")

    if shooting_pct is None:
        print("Complete TODO 3 to display shooting percentage.")
    else:
        print(f"Shooting percentage: {shooting_pct:.2f}%")


if __name__ == "__main__":
    main()