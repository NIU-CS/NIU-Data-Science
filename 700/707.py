# 707

x_subjects = set()
print("Enter subjects for group X (type 'end' to stop):")
while (sub := input()) != "end":
    x_subjects.add(sub)

y_subjects = set()
print("Enter subjects for group Y (type 'end' to stop):")
while (sub := input()) != "end":
    y_subjects.add(sub)

print(f"All subjects: {sorted(x_subjects | y_subjects)}")
print(f"Common subjects: {sorted(x_subjects & y_subjects)}")
print(f"Subjects in Y but not in X: {sorted(y_subjects - x_subjects)}")
print(f"Unique subjects: {sorted(x_subjects ^ y_subjects)}")
