# 709

color_dict = {}
print("Enter color dictionary (key 'end' to stop):")
while (key := input("Key: ")) != "end":
    value = input("Value: ")
    color_dict[key] = value

sorted_dict = dict(sorted(color_dict.items()))
for key, value in sorted_dict.items():
    print(f"{key}: {value}")
