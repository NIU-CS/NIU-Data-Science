# 310

import math

n = int(input())
total = 0

for i in range(1, n):
    total += 1 / (math.sqrt(i) + math.sqrt(i + 1))

print(f"{total:.4f}")
