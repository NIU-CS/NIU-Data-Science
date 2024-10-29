# 606

rows, cols = int(input()), int(input())
matrix = [[col - row for col in range(cols)] for row in range(rows)]
for row in matrix:
    print(" ".join(f"{num:4}" for num in row))
