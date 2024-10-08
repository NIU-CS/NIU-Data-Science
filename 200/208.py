# 208


def decimal_to_hexadecimal(num):
    if 0 <= num <= 15:
        return hex(num)[2:].upper()  # 使用內建的 hex 函數並移除 '0x' 前綴
    else:
        return "請輸入 0 到 15 之間的數值"


# 輸入十進位數值
num = int(input("請輸入一個十進位整數(0 <= num <= 15): "))
# 將十進位轉換為十六進位
result = decimal_to_hexadecimal(num)
print(f"十六進位的值為: {result}")
