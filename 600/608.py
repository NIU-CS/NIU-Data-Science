# 608

matrix = [[int(input()) for _ in range(3)] for _ in range(3)]

max_value = max(max(row) for row in matrix)
min_value = min(min(row) for row in matrix)

max_index = [
    (i, j)
    for i, row in enumerate(matrix)
    for j, val in enumerate(row)
    if val == max_value
][0]
min_index = [
    (i, j)
    for i, row in enumerate(matrix)
    for j, val in enumerate(row)
    if val == min_value
][0]

print(f"Index of the largest number {max_value} is: {max_index}")
print(f"Index of the smallest number {min_value} is: {min_index}")
