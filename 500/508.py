# 508

def compute(x, y):
    while y != 0:
        x, y = y, x % y
    return x

x = int(input("Input the first positive integer: "))
y = int(input("Input the second positive interger: "))

gcd = compute(x, y)
print(f"The gcd of {x} and {y} is: {gcd}")
