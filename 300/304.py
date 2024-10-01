# 304

a = int(input("Enter an integer: "))
total = sum(i for i in range(1, a + 1) if i % 5 == 0)
print(total)
