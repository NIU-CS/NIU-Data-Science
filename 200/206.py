def grade_classification(score):
    if 80 <= score <= 100:
        return "A"
    elif 70 <= score <= 79:
        return "B"
    elif 60 <= score <= 69:
        return "C"
    else:
        return "F"


# 輸入分數
score = int(input("請輸入分數: "))
# 判斷等級並輸出
grade = grade_classification(score)
print(f"等級: {grade}")
