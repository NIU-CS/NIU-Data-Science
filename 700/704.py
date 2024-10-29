# 704

num_set = set()
while True:
    num = int(input())
    if num == -9999:
        break
    num_set.add(num)

print(f"Length: {len(num_set)}")
print(f"Max: {max(num_set)}")
print(f"Min: {min(num_set)}")
print(f"Sum: {sum(num_set)}")
