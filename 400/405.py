# 405

def get_gpa(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'E'

while True:
    score = int(input())
    if score == -9999:
        break
    print(get_gpa(score))
