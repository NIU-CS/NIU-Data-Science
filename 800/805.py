# 805

def main():
    user_input = input()

    if len(user_input) != 6:
        print("Length of input should be 6")
        return

    left_aligned = f"|{user_input:<10}|"
    center_aligned = f"|{user_input:^10}|"
    right_aligned = f"|{user_input:>10}|"

    print(left_aligned)
    print(center_aligned)
    print(right_aligned)

if __name__ == "__main__":
    main()
