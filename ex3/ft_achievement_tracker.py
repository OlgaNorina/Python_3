import random

ALL_ACHIEVEMENTS = [
    'Crafting Genius', 'World Savior', 'Master Explorer',
    'Collector Supreme', 'Untouchable', 'Boss Slayer',
    'Speedrunner', 'Treasure Hunter', 'First Blood', 'PvP God',
    'Lore Master', 'Shadow Ninja', 'Rich individual', 'Undead Slayer'
]


def gen_player_achievements() -> set[str]:
    """Generates a random set of achievements for a player.
    Selects a random sample of achievements

    Returns:
        set[str]: A set of unique achievements names
    """
    all_set: set[str] = set(ALL_ACHIEVEMENTS)

    count = random.randint(1, len(all_set))

    achievement_list = random.sample(ALL_ACHIEVEMENTS, count)
    return set(achievement_list)


def get_unique_achievements(
    players_data: dict[str, set[str]],
    target_name: str
) -> set[str]:
    """Finds achievements that are earned by a single player

    Args:
        players_data: A dictionary mapping player names
        target_name: A name of the player to analyze

    Returns:
        set[str]: A set of achievements unique to the target player.
    """

    other_union: set[str] = set()
    for name in players_data:
        if name != target_name:
            other_union = other_union.union(players_data[name])

    return players_data[target_name].difference(other_union)


def main() -> None:
    """Simulates achievement tracking for a group of players."""
    print("=== Achievement Tracker System ===\n")
    players_list: list[str] = ['Alice', 'Bob', 'Charlie', 'Dylan']
    players_data: dict[str, set[str]] = {}

    for name in players_list:
        players_data[name] = gen_player_achievements()
        print(f"Player {name}: {players_data[name]}")

    all_players_achievements: set[str] = set()
    for achievement in players_data.values():
        all_players_achievements.update(achievement)
    print(f"\nAll distinct achievements: {all_players_achievements}")

    common = players_data[players_list[0]]
    for name in players_list[1:]:
        common = common.intersection(players_data[name])
    print(f"\nCommon achievements: {common}\n")

    for name in players_data:
        unique: set[str] = get_unique_achievements(players_data, name)
        print(f"Only {name} has: {unique}")

    print("\n")
    full_set: set[str] = set(ALL_ACHIEVEMENTS)
    for name in players_data:
        print(f"{name} is missing: {full_set.difference(players_data[name])}")


if __name__ == "__main__":
    main()
