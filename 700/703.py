# 703

str_list = []
while True:
    s = input()
    if s == "end":
        break
    str_list.append(s)

tup = tuple(str_list)
print(tup)
print(tup[:3])
print(tup[-3:])
