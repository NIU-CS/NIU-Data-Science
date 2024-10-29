# 705

print("Input to set1:")
set1 = {int(input()) for _ in range(5)}

print("Input to set2:")
set2 = {int(input()) for _ in range(3)}

print("Input to set3:")
set3 = {int(input()) for _ in range(9)}

is_subset = set2.issubset(set1)
is_superset = set3.issuperset(set1)

print(f"set2 is subset of set1: {is_subset}")
print(f"set3 is superset of set1: {is_superset}")
