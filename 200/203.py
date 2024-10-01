# 203

def is_leap_year(year):
    # 若年份能被4整除且不能被100整除，或能被400整除，則為閏年
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# 輸入西元年份
year = int(input("請輸入西元年份: "))

# 判斷是否為閏年
if is_leap_year(year):
    print(f"{year} 是閏年。")
else:
    print(f"{year} 不是閏年。")
