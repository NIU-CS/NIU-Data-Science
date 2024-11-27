# 904


def read_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()
    return lines


def parse_data(lines):
    data = []
    for line in lines:
        name, height, weight = line.split()
        height = float(height)
        weight = float(weight)
        data.append((name, height, weight))
    return data


def calculate_averages(data):
    total_height = sum(person[1] for person in data)
    total_weight = sum(person[2] for person in data)
    avg_height = total_height / len(data)
    avg_weight = total_weight / len(data)
    return avg_height, avg_weight


def find_extremes(data):
    tallest = max(data, key=lambda x: x[1])
    heaviest = max(data, key=lambda x: x[2])
    return tallest, heaviest


def main():
    file_path = "read.txt"
    lines = read_file(file_path)
    data = parse_data(lines)

    for person in data:
        print(f"{person[0]} {person[1]} {person[2]}\n")

    avg_height, avg_weight = calculate_averages(data)
    print(f"Average height: {avg_height:.2f}")
    print(f"Average weight: {avg_weight:.2f}")

    tallest, heaviest = find_extremes(data)
    print(f"The tallest is {tallest[0]} with {tallest[1]}")
    print(f"The heaviest is {heaviest[0]} with {heaviest[2]}")


if __name__ == "__main__":
    main()
