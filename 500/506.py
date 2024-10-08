# 506

import math


def compute(a, b, c):
    D = b**2 - 4 * a * c

    if D > 0:
        root1 = (-b + math.sqrt(D)) / (2 * a)
        root2 = (-b - math.sqrt(D)) / (2 * a)
        return sorted([root1, root2])
    elif D == 0:
        root = -b / (2 * a)
        return [root]
    else:
        return None


a = int(input("Input the coefficient a: "))
b = int(input("Input the coefficient b: "))
c = int(input("Input the coefficient c: "))

result = compute(a, b, c)

if result is None:
    print("Your equation has no root.")
else:
    print(f"The result of the equation is: {', '.join(map(str, result))}")
