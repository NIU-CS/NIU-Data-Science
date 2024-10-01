# 210

def triangle_judgment(a, b, c):
    # 檢查是否可以構成三角形
    if a + b > c and a + c > b and b + c > a:
        perimeter = a + b + c  # 計算周長
        return perimeter
    else:
        return "Invalid"

# 輸入三個邊長
a = float(input("請輸入第一個邊長: "))
b = float(input("請輸入第二個邊長: "))
c = float(input("請輸入第三個邊長: "))

# 判斷並輸出結果
result = triangle_judgment(a, b, c)
print(result)
