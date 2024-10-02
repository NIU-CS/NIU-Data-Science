# 406

while True:
    height = float(input())
    if height == -9999:
        break
    weight = float(input())
    if weight == -9999:
        break
    bmi = weight / (height / 100) ** 2
    if bmi < 18.5:
        state = "under weight"
    elif bmi < 24:
        state = "normal"
    elif bmi < 27:
        state = "over weight"
    else:
        state = "fat"
    print(f"BMI: {bmi:.2f}")
    print(f"State: {state}")
