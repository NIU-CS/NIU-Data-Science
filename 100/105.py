# 105


def calculate_rectangle(width, height):
    perimeter = 2 * (width + height)  # 計算周長
    area = width * height  # 計算面積

    # 輸出格式化結果，保留兩位小數
    print(f"Height = {height:.2f}")
    print(f"Width = {width:.2f}")
    print(f"Perimeter = {perimeter:.2f}")
    print(f"Area = {area:.2f}")


# 輸入矩形的寬和高
height = float(input("Enter height: "))
width = float(input("Enter width: "))

# 呼叫計算函式
calculate_rectangle(width, height)
