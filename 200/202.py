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


# 輸入一個整數
x = int(input("Enter a number: "))

# 呼叫倍數判斷函式
check_multiple(x)
