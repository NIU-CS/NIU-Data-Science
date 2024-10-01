# 104

import math

def calculate_circle(radius):
    perimeter = 2 * math.pi * radius  # 計算周長
    area = math.pi * radius ** 2  # 計算面積

    # 輸出格式化結果，保留兩位小數
    print(f"Radius = {radius:.2f}")
    print(f"Perimeter = {perimeter:.2f}")
    print(f"Area = {area:.2f}")

# 輸入圓的半徑
radius = float(input())

# 呼叫計算函式
calculate_circle(radius)
