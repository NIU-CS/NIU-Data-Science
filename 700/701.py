# 701

lst = []
while True:
    num = int(input())
    if num == -9999:
        break
    lst.append(num)

tup = tuple(lst)
print(tup)
print(f"Length: {len(tup)}")
print(f"Max: {max(tup)}")
print(f"Min: {min(tup)}")
print(f"Sum: {sum(tup)}")
