# 609

print("Enter matrix 1:")
matrix1 = [[int(input(f"[{i+1}, {j+1}]: ")) for j in range(2)] for i in range(2)]

print("Enter matrix 2:")
matrix2 = [[int(input(f"[{i+1}, {j+1}]: ")) for j in range(2)] for i in range(2)]

print("Matrix 1:")
for row in matrix1:
    print(" ".join(map(str, row)))

print("Matrix 2:")
for row in matrix2:
    print(" ".join(map(str, row)))

sum_matrix = [[matrix1[i][j] + matrix2[i][j] for j in range(2)] for i in range(2)]

print("Sum of 2 matrices:")
for row in sum_matrix:
    print(" ".join(map(str, row)))
