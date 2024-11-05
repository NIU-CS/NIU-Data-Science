# 106


def calculate_speed(x_minutes, y_seconds, z_km):
    total_time_in_hours = x_minutes / 60 + y_seconds / 3600
    z_miles = z_km / 1.6
    speed = z_miles / total_time_in_hours
    print(f"Speed = {speed:.1f}")


x_minutes = int(input())
y_seconds = int(input())
z_km = float(input())

calculate_speed(x_minutes, y_seconds, z_km)
