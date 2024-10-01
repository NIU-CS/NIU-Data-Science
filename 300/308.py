# 308

test_cases = int(input("Enter number of test cases: "))
for _ in range(test_cases):
    n = int(input("Enter an integer: "))
    total = sum(int(digit) for digit in str(n))
    print(f"Sum of all digits of {n} is {total} ")
