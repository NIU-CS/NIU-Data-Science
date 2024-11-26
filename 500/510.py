# 510


def compute(num):
    fibonacci_sequence = [0, 1]

    for i in range(2, num):
        next_value = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_value)

    return fibonacci_sequence


def print_result(fibonacci_sequence):
    for value in fibonacci_sequence:
        print(f"{value}", end=" ")


num = int(input())

print_result(compute(num))
