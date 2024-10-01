# 302

a = int(input("Enter the starting integer: "))
b = int(input("Enter the ending integer: "))
total = sum(i for i in range(a, b + 1) if i % 2 == 0)
print(total)
