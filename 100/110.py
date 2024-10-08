# 110

import math


def calculate_polygon_area(n, s):
    # 使用公式計算正 n 邊形的面積
    area = (n * math.pow(s, 2)) / (4 * math.tan(math.pi / n))

    # 輸出格式化結果，保留四位小數
    print(f"Area = {area:.4f}")


# 輸入正 n 邊形的邊數和邊長
n = int(input("Enter the number of sides (n): "))
s = float(input("Enter the side length (s): "))

# 呼叫計算函式
calculate_polygon_area(n, s)
