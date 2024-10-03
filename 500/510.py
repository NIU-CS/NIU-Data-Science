#510
def compute(num):
    fibonacci_sequence = [0, 1]

    for i in range(2, num):
        next_value = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_value)

    return fibonacci_sequence

num = int(input("Input a positive integer num (num >= 2): "))

result = compute(num)
print(f"The front {num} number of fibonacci_sequence is: {result}")