import random
import typing


PLAYERS_LIST: list[str] = [
    "bob", "alice", "dylan", "charlie"
]

ACTIONS_LIST: list[str] = [
    "run", "eat", "sleep", "climb", "move",
    "release", "grab", "use"
]


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    """Generates random events for players

    Yields:
        Generator of tuple[str, str]
    """
    while True:
        yield random.choice(PLAYERS_LIST), random.choice(ACTIONS_LIST)


def consume_event(
    events: list[tuple[str, str]]
) -> typing.Generator[tuple[str, str], None, None]:
    """Randomly yields and removes events from the list until it is empty.

    Args:
        events: A list of event tuples (player name, action).

    Yields:
        A randomly selected event tuple.
    """
    while events:
        index: int = random.randrange(len(events))
        current_event: tuple[str, str] = events[index]
        print(f"Got event from list: {current_event}")
        del events[index]
        yield current_event


def main() -> None:
    name: str
    action: str

    print("=== Game Data Stream Processor ===")
    event_stream = gen_event()
    for i in range(1000):
        name, action = next(event_stream)
        print(f"Event {i}: Player {name} did action {action}")

    build_list: list[tuple[str, str]] = []
    for i in range(10):
        build_list = build_list + [next(gen_event())]
    print(f"Built list of 10 events: {build_list}")

    for event in consume_event(build_list):
        print(f"Remains in list: {build_list}")


if __name__ == "__main__":
    main()
