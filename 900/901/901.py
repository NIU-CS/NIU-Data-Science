# 901


def main():
    with open("write.txt", "w", encoding="utf-8") as file:
        for i in range(5):
            data = input()
            file.write(data + "\n")


if __name__ == "__main__":
    main()
