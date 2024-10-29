# 604

from collections import Counter
numbers = [int(input()) for _ in range(10)]
count = Counter(numbers)
mode, frequency = count.most_common(1)[0]
print(f"{mode} {frequency}")
