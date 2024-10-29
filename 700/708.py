# 708

dict1 = {}
print("Enter key-value pairs for dict1 (key 'end' to stop):")
while (key := input("Key: ")) != "end":
    value = input("Value: ")
    dict1[key] = value

dict2 = {}
print("Enter key-value pairs for dict2 (key 'end' to stop):")
while (key := input("Key: ")) != "end":
    value = input("Value: ")
    dict2[key] = value

combined_dict = {**dict1, **dict2}
sorted_dict = dict(sorted(combined_dict.items()))
for key, value in sorted_dict.items():
    print(f"{key}: {value}")
