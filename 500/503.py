#503
def compute(a, b):
    return sum(range(a, b + 1))

a = int(input("Input the first integer (a): "))
b = int(input("Input the second interger (b): "))

result = compute(a, b)
print(f"\nthe sum from {a} to {b} is: {result}")