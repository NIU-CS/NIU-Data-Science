# 205

# 輸入一個字元
char = input("請輸入一個字元: ")

# 判斷字元是否為英文大小寫字母
if char.isalpha():
    print(f"{char} is an alphabet.")
# 判斷字元是否為數字
elif char.isdigit():
    print(f"{char} is a number.")
# 判斷字元是否為符號
else:
    print(f"{char} is a symbol.")
