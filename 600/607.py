# 607

scores_list = []

for student_id in range(1, 4):
    print(f"The {student_id}st student:")
    scores = [int(input()) for _ in range(5)]
    scores_list.append(scores)

for student_id, scores in enumerate(scores_list, start=1):
    total = sum(scores)
    average = total / len(scores)
    print(f"Student {student_id}")
    print(f"#Sum {total}")
    print(f"#Average {average:.2f}")
