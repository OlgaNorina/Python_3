import sys

def ft_score_analytics() -> None:
    """Processes raw string arguments individually.

    Discards invalid inputs while printing error messages.
    """
    total_args: int = len(sys.argv)
    score_list: list[int] = []

    i: int = 1
    while i < total_args:
        arg: int = sys.argv[i]
        try:
            score_list = score_list + [int(arg)]
        except ValueError:
            print(f"Invalid parameter: '{arg}'")
        i += 1

    total_players: int = len(score_list)
    if total_players == 0:
        print(
                "No scores provided. Usage: python3 ft_score_analytics.py "
                "<score1> <score2> ..."
                )
        return
    score_sum: int = 0
    score_max: int = score_list[1]
    score_min: int = score_list[1]
    i = 0


    while i < total_players:
        score_sum += score_list[i]
        if score_max < score_list[i]:
            score_max = score_list[i]
        if score_min > score_list[i]:
            score_min = score_list[i]
        i += 1

    print("=== Player Score Analytics ===")
    print(f"Scores processed: {score_list}")
    print(f"Total players: {total_players}")
    print(f"Total score: {score_sum}")
    print(f"Average score: {score_sum / total_players:.1f}")
    print(f"High score: {score_max}")
    print(f"Low score: {score_min}")
    print(f"Score range: {score_max - score_min}")


if __name__ == "__main__":
    ft_score_analytics()

