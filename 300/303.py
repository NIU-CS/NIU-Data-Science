# 303

n = int(input("Enter an integer (<100): "))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(f"{i * j:4}", end="")
    print()
