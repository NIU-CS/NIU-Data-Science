# 201


def is_even(number):
    if number % 2 == 0:
        print(f"{number} is an even number.")
    else:
        print(f"{number} is not an even number.")


# 輸入一個正整數
number = int(input("Enter a number: "))

# 呼叫偶數判斷函式
is_even(number)
