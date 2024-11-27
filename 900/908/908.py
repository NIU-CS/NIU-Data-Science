# 908

from collections import Counter


def main():
    file_name = input()
    target_count = int(input())

    try:
        with open(file_name, "r", encoding="utf-8") as file:
            content = file.read()

        words = content.split()
        word_counts = Counter(words)

        matching_words = [
            word for word, count in word_counts.items() if count == target_count
        ]
        matching_words.sort(key=lambda x: x.lower())

        for word in matching_words:
            print(word)
    except FileNotFoundError:
        print(f"錯誤: 檔案 {file_name} 不存在。")


if __name__ == "__main__":
    main()
