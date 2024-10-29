# 710

search_dict = {}
print("Enter dictionary (key 'end' to stop):")
while (key := input("Key: ")) != "end":
    value = input("Value: ")
    search_dict[key] = value

search_key = input("Enter key to search: ")
print("Key exists." if search_key in search_dict else "Key does not exist.")
