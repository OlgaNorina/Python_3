import random


PLAYERS_LIST: list[str] = [
    'Alice', 'bob', 'Charlie', 'dylan',
    'Emma', 'Gregory', 'john', 'kevin', 'Liam'
]


def main() -> None:
    """Processes player names and analyzes their randomized high scores."""
    print("=== Game Data Alchemist ===\n")
    print(f"Initial list of players: {PLAYERS_LIST}")
    capitalized_list: list[str] = [
        string.capitalize()for string in PLAYERS_LIST
    ]
    print(f"New list with all names capitalized: {capitalized_list}")

    list_capitalized_name: list[str] = [
        string for string in PLAYERS_LIST if string.istitle()
    ]
    print(f"New list of capitalized names only: {list_capitalized_name}")

    score_dict: dict[str, int] = {
        string: random.randint(1, 1000) for string in capitalized_list
        }
    print(f"\nScore dict: {score_dict}")

    if len(score_dict) > 0:
        score_average: float = sum(score_dict.values()) / len(score_dict)
        print(f"Score average: {score_average:.2f}")

    high_score_dict: dict[str, int] = {
        string: score for string, score in score_dict.items()
        if score > score_average
        }
    print(f"High scores: {high_score_dict}")


if __name__ == "__main__":
    main()
