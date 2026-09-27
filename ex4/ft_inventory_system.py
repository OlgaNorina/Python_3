import sys


def ft_inventory_system() -> dict[str, int]:
    """Parses the command-line parameters
        to fill the inventory

    Returns:
        dict[str, int]: The cleaned inventory dictionary.
    """
    inventory: dict[str, int] = {}

    for arg in sys.argv[1:]:
        if ":" not in arg:
            print(f"Error - invalid parameter '{arg}")
            continue

        one_inv: list[str] = arg.split(":", 1)
        key: str = one_inv[0].strip()
        value: str = one_inv[1].strip()

        if key in inventory:
            print(f"Redundant item '{key}' - discarding")
            continue

        try:
            quantity: int = int(value)
            if quantity < 0:
                print(f"Quantity error for '{key}': cannot be negative")
                continue
            inventory[key] = quantity
        except ValueError as err:
            print(f"Quantity error for '{key}': {err}")

    return inventory


def inventory_analyze(inventory: dict[str, int]) -> None:
    """Analyze and prints inventory statistics.

    Args:
        inventory: The inventory to analyze
    """

    amount: int = sum(inventory.values())

    print(f"Total quantity of the {len(inventory)} items: {amount}")

    for key in inventory:
        percetage = round(
            (inventory[key] / amount) * 100, 1
            ) if amount > 0 else 0.0
        print(f"Item {key} represents {percetage}%")

    max_inv: int = -1
    min_inv: int = sys.maxsize
    most_abundant: str = ""
    least_abundant: str = ""

    for key in inventory:
        inv: int = inventory[key]
        if inv > max_inv:
            max_inv = inv
            most_abundant = key

        if inv < min_inv:
            min_inv = inv
            least_abundant = key

    print(f"Item most abundant: {most_abundant} with quantity {max_inv}")
    print(f"Item least abundant: {least_abundant} with quantity {min_inv}")


def main() -> None:
    inventory = ft_inventory_system()
    if not inventory:
        return

    print("=== Inventory System Analysis ===")
    print(f"Got inventory: {inventory}")
    print(f"Item list: {list(inventory.keys())}")

    inventory_analyze(inventory)

    inventory.update({"magic_item": 1})
    print(f"Update inventory: {inventory}")


if __name__ == "__main__":
    main()
