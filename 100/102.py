# 102


def format_output_floats(numbers):
    print(f"|{numbers[0]:>7.2f} {numbers[1]:>7.2f}|")
    print(f"|{numbers[2]:>7.2f} {numbers[3]:>7.2f}|")
    print(f"|{numbers[0]:<7.2f} {numbers[1]:<7.2f}|")
    print(f"|{numbers[2]:<7.2f} {numbers[3]:<7.2f}|")


numbers = []
for _ in range(4):
    numbers.append(float(input()))

format_output_floats(numbers)
