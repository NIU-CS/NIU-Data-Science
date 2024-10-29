# 605

scores = [int(input()) for _ in range(10)]
scores.remove(max(scores))
scores.remove(min(scores))
print(sum(scores))
print(f"{sum(scores)/len(scores):.2f}")
