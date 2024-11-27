# 906


def main():
    file_name = input()
    s1 = input()
    s2 = input()

    try:
        with open(file_name, "r", encoding="utf-8") as file:
            content = file.read()
        print("=== Before the replacement")
        print(content)

        updated_content = content.replace(s1, s2)
        print("\n=== After the replacement")
        print(updated_content)

        with open(file_name, "w", encoding="utf-8") as file:
            file.write(updated_content)
    except FileNotFoundError:
        print(f"錯誤: 檔案 {file_name} 不存在。")


if __name__ == "__main__":
    main()
