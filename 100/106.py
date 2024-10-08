# 106


def calculate_speed(x_minutes, y_seconds, z_km):
    # 將時間轉換為小時
    total_time_in_hours = x_minutes / 60 + y_seconds / 3600
    # 將公里轉換為英里
    z_miles = z_km / 1.6
    # 計算速度
    speed = z_miles / total_time_in_hours

    # 輸出格式化結果，保留一位小數
    print(f"Speed = {speed:.1f}")


# 輸入 x 分鐘, y 秒和 z 公里
x_minutes = int(input("Enter minutes: "))
y_seconds = int(input("Enter seconds: "))
z_km = float(input("Enter kilometers: "))

# 呼叫計算函式
calculate_speed(x_minutes, y_seconds, z_km)
