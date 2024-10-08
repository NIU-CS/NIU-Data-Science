# 403

a = int(input())
b = int(input())
multiples = [x for x in range(a, b + 1) if x % 4 == 0 or x % 9 == 0]
for i in range(0, len(multiples), 10):
    print(" ".join(f"{x:<4}" for x in multiples[i : i + 10]))
print(f"Multiples count: {len(multiples)}")
print(f"Sum: {sum(multiples)}")
