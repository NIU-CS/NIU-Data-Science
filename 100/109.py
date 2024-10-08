# 109

import math


def calculate_pentagon_area(s):
    # 使用公式計算正五邊形面積
    area = (5 * math.pow(s, 2)) / (4 * math.tan(math.pi / 5))

    # 輸出格式化結果，保留四位小數
    print(f"Area = {area:.4f}")


# 輸入正五邊形的邊長
s = float(input("Enter the side length of the pentagon: "))

# 呼叫計算函式
calculate_pentagon_area(s)
