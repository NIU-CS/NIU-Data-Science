# 907

def main():
    file_name = input()

    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        line_count = len(lines)
        word_count = sum(len(line.split()) for line in lines)
        char_count = sum(len(line.replace(" ", "").replace("\n", "")) for line in lines)
        
        print(f"{line_count} line(s)")
        print(f"{word_count} word(s)")
        print(f"{char_count} character(s)")
    except FileNotFoundError:
        print(f"錯誤: 檔案 {file_name} 不存在。")

if __name__ == "__main__":
    main()