# 202


def check_multiple(x):
    if x % 3 == 0 and x % 5 == 0:
        print(f"{x} is a multiple of 3 and 5.")
    elif x % 3 == 0:
        print(f"{x} is a multiple of 3.")
    elif x % 5 == 0:
        print(f"{x} is a multiple of 5.")
    else:
        print(f"{x} is not a multiple of 3 or 5.")


x = int(input())

check_multiple(x)
