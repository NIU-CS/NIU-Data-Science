# 209

import math


def distance_judgment(x, y):
    x1, y1 = 5, 6  # 參考點的座標
    distance = math.sqrt((x - x1) ** 2 + (y - y1) ** 2)  # 計算兩點距離
    if distance <= 15:
        return "Inside"
    else:
        return "Outside"


# 輸入平面座標
x = float(input("請輸入x座標: "))
y = float(input("請輸入y座標: "))

# 判斷距離並輸出結果
result = distance_judgment(x, y)
print(result)
