# 107


def calculate_values(numbers):
    total = sum(numbers)  # 計算總和
    average = total / len(numbers)  # 計算平均值

    # 輸出所有數字
    print(" ".join(map(str, numbers)))
    # 輸出總和和平均值，保留小數點後一位
    print(f"Sum = {total:.1f}")
    print(f"Average = {average:.1f}")


# 輸入五個數字
numbers = []
for _ in range(5):
    number = float(input("Enter a number: "))
    numbers.append(number)

# 呼叫計算函式
calculate_values(numbers)
