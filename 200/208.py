# 208


def decimal_to_hexadecimal(num):
    if 0 <= num <= 15:
        return hex(num)[2:].upper()
    else:
        return "請輸入 0 到 15 之間的數值"


num = int(input())
print(decimal_to_hexadecimal(num))
