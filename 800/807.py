# 807


def main():
    user_input = input()
    numbers = list(map(int, user_input.split()))

    if len(numbers) != 5:
        print("Please enter 5 numbers")
        return

    total = sum(numbers)
    average = total / len(numbers)

    print(f"{total}")
    print(f"{average:.1f}")


if __name__ == "__main__":
    main()
