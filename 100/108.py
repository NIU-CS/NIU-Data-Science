# 108

import math


def calculate_distance(x1, y1, x2, y2):
    # 計算歐式距離
    distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    # 輸出座標及距離，距離保留四位小數
    print(f"({x1}, {y1})")
    print(f"({x2}, {y2})")
    print(f"Distance = {distance:.4f}")


# 輸入 x1, y1, x2, y2 四個數字
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

# 呼叫計算函式
calculate_distance(x1, y1, x2, y2)
