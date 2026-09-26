import random

ALL_ACHIEVEMENTS = [
        'Crafting Genius', 'World Savior', 'Master Explorer',
        'Collector Supreme', 'Untouchable', 'Boss Slayer',
        'Speedrunner', 'Treasure Hunter', 'First Blood', 'PvP God',
        'Lore Master', 'Shadow Ninja', 'Rich individual', 'Undead Slayer'
        ]


def gen_player_achievement_tracker() -> set:
    all_set: set = set(ALL_ACHIEVEMENTS)

    count = random.randint(1, len(all_set))

    achievement_list = random.sample(ALL_ACHIEVEMENTS, count)
    return set(achievement_list)


def get_unique_achievements(players_data, target_name) -> set:
    other_union: set = set()
    for name in players_data:
        if name != target_name:
            others_union = other_union.union(players_data[name])

    return players_data[target_name].difference(others_union)


def main() -> None:
    players_list: list[str] = ['Alice', 'Bob', 'Charlie', 'Dylan']
    players_data: dict = {}

    for name in players_list:
        players_data[name] = gen_player_achievement_tracker()
        print(f"Player {name}: {players_data[name]}")

    common = players_data[players_list[0]]
    for name in players_list[1:]:
        common = common.intersection(players_data[name])
    print(f"\nCommon achievements: {common}\n")

    for name in players_data:
        unique: set = get_unique_achievements(players_data, name)
        print(f"Only {name} has: {unique}")
    
    print("\n")
    full_set: set = set(ALL_ACHIEVEMENTS)
    for name in players_data:
        print(f"{name} is missing: {full_set.difference(players_data[name])}")



if __name__ == "__main__":
    main()
