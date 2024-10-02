# 408

numbers = [int(input()) for _ in range(10)]
odd_count = sum(1 for x in numbers if x % 2 != 0)
even_count = 10 - odd_count
print(f"Odd numbers: {odd_count}")
print(f"Even numbers: {even_count}")
