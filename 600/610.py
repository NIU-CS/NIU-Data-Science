# 610

temperatures = []

for week in range(1, 5):
    print(f"Week {week}:")
    weekly_temperatures = []
    for day in range(1, 4):
        temp = float(input(f"Day {day}: "))
        weekly_temperatures.append(temp)
    temperatures.extend(weekly_temperatures)

average_temp = sum(temperatures) / len(temperatures)
highest_temp = max(temperatures)
lowest_temp = min(temperatures)

print(f"Average: {average_temp:.2f}")
print(f"Highest: {highest_temp:.1f}")
print(f"Lowest: {lowest_temp:.1f}")
