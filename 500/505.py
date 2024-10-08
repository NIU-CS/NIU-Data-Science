# 505


def compute(a, x, y):
    for _ in range(y):
        print((a + " ") * x)


a = input("Input a character: ")
x = int(input("Input cols: "))
y = int(input("Input rows: "))

compute(a, x, y)
