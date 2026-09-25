import sys


def main() -> None:
    print("=== Command Quest ===")

    program_name = sys.argv[0]
    print(f"Program name: {program_name}")

    total_args: int = len(sys.argv)
    arg_count: int = total_args - 1

    if arg_count == 0:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {arg_count}")
        index: int = 1
        while index < total_args:
            print(f"Argument {index}: {sys.argv[index]}")
            index += 1
    print(f"Total arguments: {total_args}")


if __name__ == "__main__":
    main()
