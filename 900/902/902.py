# 902


def main():
    total = 0
    with open("read.txt", "r", encoding="utf-8") as file:
        content = file.read()
        numbers = map(int, content.split())
        total = sum(numbers)

    print(f"{total}")


if __name__ == "__main__":
    main()
