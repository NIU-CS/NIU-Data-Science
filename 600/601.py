# 601

numbers = [int(input()) for _ in range(12)]

for i in range(0, len(numbers), 3):
    print("".join(f"{num:3}" for num in numbers[i:i+3]))

even_index_sum = sum(numbers[i] for i in range(0, len(numbers), 2))
print(even_index_sum)
