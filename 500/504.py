#504
def compute(a, b):
    return a ** b

a = int(input("Input the first integer (a): "))
b = int(input("Input the second interger (b): "))

result = compute(a, b)
print(f"\n{a} raised to the power of {b} is: {result}")