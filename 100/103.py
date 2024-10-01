# 103

def format_output_strings(words):
    # 第一列靠右對齊，第二列靠左對齊
    print(f"|{words[0]:>10} {words[1]:>10}|")
    print(f"|{words[2]:>10} {words[3]:>10}|")
    print(f"|{words[0]:<10} {words[1]:<10}|")
    print(f"|{words[2]:<10} {words[3]:<10}|")

# 輸入四個單字
words = []
for _ in range(4):
    words.append(input())

# 呼叫格式化輸出函式
format_output_strings(words)
