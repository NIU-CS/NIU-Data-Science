# 204

# 定義一個函式來進行運算
def calculate(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        return a / b
    elif operator == '//':
        return a // b
    elif operator == '%':
        return a % b
    else:
        return "不支援的運算符號"

# 讓使用者輸入兩個整數和運算符號
a = int(input("請輸入第一個整數："))
b = int(input("請輸入第二個整數："))
operator = input("請輸入運算符號 (+, -, *, /, //, %)：")

# 呼叫函式進行運算並輸出結果
result = calculate(a, b, operator)
print(f"計算結果：{result}")
