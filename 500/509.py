#509
def compute(x, y):
    while y != 0:
        x, y = y, x % y
    return x

x = int(input("Input the first numerator: "))
y = int(input("Input the first denominator: "))
m = int(input("Input the second numerator: "))
n = int(input("Input the second denominator: "))

p = x * n + m * y
q = y * n

gcd = compute(p, q)

p_simplified = p // gcd
q_simplified = q // gcd

print(f"The sum of two fracitons is: {p_simplified}/{q_simplified}")