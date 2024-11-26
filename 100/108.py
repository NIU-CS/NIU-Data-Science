# 108

import math


def calculate_distance(x1, y1, x2, y2):
    distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    print(f"Distance = {distance:.4f}")


x1 = input()
y1 = input()
x2 = input()
y2 = input()

print(f"( {x1} , {y1} )")
print(f"( {x2} , {y2} )")

x1 = float(x1)
y1 = float(y1)
x2 = float(x2)
y2 = float(y2)

calculate_distance(x1, y1, x2, y2)
