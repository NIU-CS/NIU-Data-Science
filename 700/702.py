# 702

print("Create tuple1:")
lst1 = []
while True:
    num = int(input())
    if num == -9999:
        break
    lst1.append(num)

print("Create tuple2:")
lst2 = []
while True:
    num = int(input())
    if num == -9999:
        break
    lst2.append(num)

tup1 = tuple(lst1)
tup2 = tuple(lst2)
unsorted_list = list(tup1 + tup2)
combined_list = sorted(unsorted_list)
print(f"Before Sorting: {tup1}, {tup2}")
print(f"After Sorting: {combined_list}")
