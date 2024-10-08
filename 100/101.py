# 101


def format_output(numbers):
    # 第一列靠右對齊，第二列靠左對齊
    print(f"|{numbers[0]:>5} {numbers[1]:>5}|")
    print(f"|{numbers[2]:>5} {numbers[3]:>5}|")
    print(f"|{numbers[0]:<5} {numbers[1]:<5}|")
    print(f"|{numbers[2]:<5} {numbers[3]:<5}|")


# 輸入四個數字
numbers = []
for _ in range(4):
    numbers.append(int(input()))

# 呼叫格式化輸出函式
format_output(numbers)
