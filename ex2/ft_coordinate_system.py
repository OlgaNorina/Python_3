import math


def get_player_pos() -> tuple[float, ...]:
    """Repeatedly prompts the user for 3D coordinates.
    Only breaks out and returns when a valid tuple.
    """
    while True:
        raw_input: str = input(
            "Enter new coordinates as float in format 'x,y,z': "
            )
        input_part: list[str] = raw_input.split(",")
        if not len(input_part) == 3:
            print("Invalid syntax")
            continue

        i: int = 0
        coordinates: tuple[float, ...] = ()
        is_valid: bool = True

        while i < 3:
            try:
                one_coordinate: float = float(input_part[i])
                coordinates = coordinates + (one_coordinate,)
            except ValueError as err:
                print(f"Error on parameter '{input_part[i]}': {err}")
                is_valid = False
            i += 1
        if is_valid:
            return coordinates


def get_distance(
    first_coordinates: tuple[float, ...],
    second_coordinates: tuple[float, ...]
) -> float:
    """Calculates the distance between two coordinates"""
    distance: float = 0

    distance = math.sqrt(
            (second_coordinates[0] - first_coordinates[0])**2 +
            (second_coordinates[1] - first_coordinates[1])**2 +
            (second_coordinates[2] - first_coordinates[2])**2
            )
    return distance


def main() -> None:
    print("Get a first set of coordinates")
    first_coordinates: tuple[float, ...] = get_player_pos()
    print(f"Got a first tuple: {first_coordinates}")
    print(
        f"It includes: "
        f"X={first_coordinates[0]}, "
        f"Y={first_coordinates[1]}, "
        f"Z={first_coordinates[2]}"
        )
    center: tuple[float, ...] = (0, 0, 0)
    print(f"Distance to center {get_distance(center, first_coordinates):.4f}")

    print("\nGet a second set of coordinates")
    second_coordinates: tuple[float, ...] = get_player_pos()
    print(
        f"Distance between the 2 sets of coordinates: "
        f"{get_distance(second_coordinates, first_coordinates):.4f}"
        )


if __name__ == "__main__":
    main()
