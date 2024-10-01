# 307

n = int(input("Enter an integer (n<10): "))
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(f"{i:>2}*{j:<2}={i*j:<4}", end=" ")
        if (i*j < 10):
            print(" ", end="")
    print()
