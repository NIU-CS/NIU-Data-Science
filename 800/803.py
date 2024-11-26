# 803


def main():
    sentence = input()
    words = sentence.split()

    if len(words) < 5:
        print("Less than 5 words")
    else:
        print(" ".join(words[-3:]))


if __name__ == "__main__":
    main()
