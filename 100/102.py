# 102


def format_output_floats(numbers):
    # 第一列靠右對齊，第二列靠左對齊，保留兩位小數
    print(f"|{numbers[0]:>7.2f} {numbers[1]:>7.2f}|")
    print(f"|{numbers[2]:>7.2f} {numbers[3]:>7.2f}|")
    print(f"|{numbers[0]:<7.2f} {numbers[1]:<7.2f}|")
    print(f"|{numbers[2]:<7.2f} {numbers[3]:<7.2f}|")


# 輸入四個浮點數
numbers = []
for _ in range(4):
    numbers.append(float(input()))

# 呼叫格式化輸出函式
format_output_floats(numbers)
