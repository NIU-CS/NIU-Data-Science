# 910

def main():
    file_name = 'read.dat'

    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        if len(lines) < 2:
            print("檔案內容不足以進行分析。")
            return
        
        headers = lines[0].strip().split()
        records = [line.strip().split() for line in lines[1:]]
        
        for line in lines:
            print(line.strip()) 
            print()
        
        male_count = sum(1 for record in records if record[headers.index("性別")] == '1')
        female_count = sum(1 for record in records if record[headers.index("性別")] == '0')
        
        print(f"Number of males: {male_count}")
        print(f"Number of females: {female_count}")
    except FileNotFoundError:
        print(f"錯誤: 檔案 {file_name} 不存在。")

if __name__ == "__main__":
    main()