from pathlib import Path
import json
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Arc, Circle, Rectangle

# Locate the dataset relative to this script.
PROJECT_FOLDER = Path(__file__).resolve().parent.parent
DATA_FILE = PROJECT_FOLDER / "data" / "shots.json"


def load_shots():
    """Read the shot records and return a pandas DataFrame."""
    with DATA_FILE.open(encoding="utf-8") as file:
        shot_data = json.load(file)

    result_set = shot_data["resultSets"][0]
    
    columns = [name.lower() for name in result_set["headers"]]

    return pd.DataFrame(
        data=result_set["rowSet"],
        columns=columns,
    )

def clean_shots(shots):
    """Keep regulation-time shots and the columns used in our lesson."""
    columns = [
        "game_id",
        "game_date",
        "shot_type",
        "shot_made_flag",
        "loc_x",
        "loc_y",
    ]

    cleaned = shots.loc[shots["period"] < 5, columns].copy()

    cleaned["game_date"] = pd.to_datetime(
        cleaned["game_date"],
        format="%Y%m%d",
    )

    return cleaned

def get_season(game_date):
    """Assign a season using the textbook's July cutoff."""
    if game_date.month > 6:
        start_year = game_date.year
    else:
        start_year = game_date.year - 1

    return f"{start_year}-{start_year + 1}"


def prepare_shots(shots):
    """Add season, shot result, and field-goal points."""
    prepared = shots.copy()

    prepared["season"] = prepared["game_date"].apply(get_season)

    prepared["shot_result"] = prepared["shot_made_flag"].map(
        {0: "Missed", 1: "Made"}
    )

    shot_values = prepared["shot_type"].map(
        {"2PT Field Goal": 2, "3PT Field Goal": 3}
    )
    prepared["points_made"] = (
        shot_values * prepared["shot_made_flag"]
    )

    return prepared

def summarize_shots(shots):
    """Summarize regulation-time shooting by game and season."""
    games = (
        shots.groupby(["season", "game_id"], as_index=False)
        .agg(
            shots_attempted=("shot_made_flag", "size"),
            shots_made=("shot_made_flag", "sum"),
            field_goal_points=("points_made", "sum"),
        )
    )

    seasons = (
        games.groupby("season")
        .agg(
            games_in_data=("game_id", "size"),
            attempts_per_game=("shots_attempted", "mean"),
            makes_per_game=("shots_made", "mean"),
            field_goal_points_per_game=("field_goal_points", "mean"),
            total_attempts=("shots_attempted", "sum"),
            total_makes=("shots_made", "sum"),
        )
    )

    seasons["field_goal_pct"] = (
        seasons["total_makes"] / seasons["total_attempts"] * 100
    )

    return games, seasons

def draw_court(ax):
    """Draw a half-court using the dataset's coordinate scale."""
    court_parts = [
        # Boundary, hoop, and backboard
        Rectangle((-250, -47.5), 500, 470, fill=False),
        Circle((0, 0), radius=7.5, fill=False),
        Rectangle((-30, -7.5), 60, 1, fill=False),

        # Paint and free-throw circle
        Rectangle((-80, -47.5), 160, 190, fill=False),
        Circle((0, 142.5), radius=60, fill=False),

        # Three-point line
        Arc((0, 0), 475, 475, theta1=22, theta2=158),
    ]

    for part in court_parts:
        part.set_edgecolor("black")
        part.set_linewidth(1)
        ax.add_patch(part)

    ax.plot([-220, -220], [-47.5, 92.5], color="black", lw=1)
    ax.plot([220, 220], [-47.5, 92.5], color="black", lw=1)

def plot_season_summary(seasons):
    """Plot and save average regulation-time field-goal points."""
    output_folder = PROJECT_FOLDER / "outputs"
    output_folder.mkdir(exist_ok=True)

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.plot(
        seasons.index,
        seasons["field_goal_points_per_game"],
        marker="o",
        color="royalblue",
    )

    ax.set(
        title="Stephen Curry: Field-Goal Points per Game by Season",
        xlabel="Season",
        ylabel="Regulation-time field-goal points per game",
    )
    ax.tick_params(axis="x", labelrotation=45)
    ax.grid(axis="y", alpha=0.3)

    fig.tight_layout()

    chart_file = output_folder / "season_scoring.png"
    fig.savefig(chart_file, dpi=150)
    print(f"\nSaved chart: {chart_file}")

    plt.show()
    plt.close(fig)

def plot_shot_locations(shots):
    """Compare shot locations for two seasons."""
    selected_seasons = ["2009-2010", "2015-2016"]
    colors = {"Missed": "lightcoral", "Made": "royalblue"}

    fig, axes = plt.subplots(
        1, 2, figsize=(12, 7), sharex=True, sharey=True
    )

    for ax, season in zip(axes, selected_seasons):
        season_shots = shots.loc[shots["season"] == season]

        for result, color in colors.items():
            attempts = season_shots.loc[
                season_shots["shot_result"] == result
            ]

            ax.scatter(
                attempts["loc_x"],
                attempts["loc_y"],
                label=result,
                color=color,
                s=12,
                alpha=0.5,
            )

        ax.set_title(
            f"{season}\n{len(season_shots):,} shot attempts"
        )
        ax.set_xlabel("Horizontal shot location")
        ax.set_xlim(-300, 300)
        draw_court(ax)
        ax.set_ylim(-100, 500)
        ax.set_aspect("equal")
        ax.legend()

    axes[0].set_ylabel("Distance along court")

    fig.suptitle(
        "Stephen Curry: Regulation-Time Shot Locations"
    )
    fig.tight_layout()

    output_folder = PROJECT_FOLDER / "outputs"
    output_folder.mkdir(exist_ok=True)

    chart_file = output_folder / "shot_locations.png"
    fig.savefig(chart_file, dpi=150)
    print(f"\nSaved chart: {chart_file}")

    plt.show()
    plt.close(fig)

def main():
    raw_shots = load_shots()
    shots = clean_shots(raw_shots)
    shots = prepare_shots(shots)
    print(f"Loaded {len(raw_shots):,} shot attempts.")
    print(f"Kept {len(shots):,} regulation-time shot attempts.")
    print(f"Excluded {len(raw_shots) - len(shots):,} overtime attempts.")

    print("\nFirst five cleaned shots:")
    print(shots.head().to_string(index=False))
    print("\nPrepared shot examples:")
    print(
        shots[
            ["game_date", "season", "shot_result", "points_made"]
        ].head().to_string(index=False)
    )
    games, seasons = summarize_shots(shots)

    print("\nSeason shooting summary:")
    print(
        seasons[
            [
                "games_in_data",
                "attempts_per_game",
                "makes_per_game",
                "field_goal_points_per_game",
                "field_goal_pct",
            ]
        ].round(2).to_string()
    )

    plot_season_summary(seasons)
    
    plot_shot_locations(shots)
    
if __name__ == "__main__":
    main()