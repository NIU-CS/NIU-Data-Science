# 909

def write_data(file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(5):
            name_phone = input()
            file.write(f"{name_phone}\n")

def read_data(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            content = file.read()
        print("The content of ""data.dat"":")
        print(content)
    except FileNotFoundError:
        print(f"錯誤: 檔案 {file_name} 不存在。")

def main():
    file_name = 'data.dat'
    write_data(file_name)
    read_data(file_name)

if __name__ == "__main__":
    main()
