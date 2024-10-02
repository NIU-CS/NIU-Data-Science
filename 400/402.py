# 402

min_value = float('inf')
while True:
    num = int(input())
    if num == 9999:
        break
    if num < min_value:
        min_value = num
print(min_value)
