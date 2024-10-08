# 207


def calculate_discount(price):
    if price >= 38000:
        discount = 0.7
    elif price >= 28000:
        discount = 0.8
    elif price >= 18000:
        discount = 0.9
    elif price >= 8000:
        discount = 0.95
    else:
        return "購物金額需達 8000 以上才享有折扣"

    final_price = price * discount
    return final_price


# 輸入購物金額
price = float(input("請輸入購物金額: "))
# 計算折扣後的金額
result = calculate_discount(price)
print(f"折扣後的金額為: {result}")
