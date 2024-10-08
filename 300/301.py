# 301


def sum_of_integers(a, b):
    total = 0
    for i in range(a, b + 1):
        total += i
    return total


# 輸入兩個整數 a 和 b
a = int(input("請輸入第一個整數 a: "))
b = int(input("請輸入第二個整數 b: "))

# 判斷 a 是否小於 b
if a < b:
    result = sum_of_integers(a, b)
    print(result)
else:
    print("錯誤: a 應小於 b")
