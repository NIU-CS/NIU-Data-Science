# 309

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (as a percentage): "))
months = int(input("Enter the number of months: "))
for month in range(1, months + 1):
    principal += principal * (rate / 100) / 12
    print(f"Month {month}: {principal:.2f}")
