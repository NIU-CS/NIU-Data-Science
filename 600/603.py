# 603

numbers = [int(input()) for _ in range(10)]
top_3 = sorted(numbers, reverse=True)[:3]
print(" ".join(map(str, top_3)))
