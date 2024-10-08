# 507


def compute(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True


x = int(input("Input a interger: "))

if compute(x):
    print("Prime")
else:
    print("Not Prime")
