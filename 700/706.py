# 706

k = int(input())
for _ in range(k):
    sentence = input("Enter a sentence: ").lower()
    is_pangram = all(chr(c) in sentence for c in range(ord("a"), ord("z") + 1))
    print(is_pangram)
