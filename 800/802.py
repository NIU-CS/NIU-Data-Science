# 802

def main():
    user_input = input()
    total_sum = 0

    for char in user_input:
        ascii_value = ord(char)
        total_sum += ascii_value
        print(f"ASCII code for '{char}' is: {ascii_value}")

    print(f"{total_sum}")

if __name__ == "__main__":
    main()
