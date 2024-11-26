# 903


def main():
    with open("data.txt", "a", encoding="utf-8") as file:
        for i in range(5):
            name = input()
            file.write(name + "\n")

    with open("data.txt", "r", encoding="utf-8") as file:
        content = file.read()
        print(content)


if __name__ == "__main__":
    main()
