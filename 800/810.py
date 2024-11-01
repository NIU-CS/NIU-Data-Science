# 810

def main():
    k = int(input())

    for i in range(k):
        numbers = list(map(float, input(f"").split()))
        max_value = max(numbers)
        min_value = min(numbers)
        difference = max_value - min_value
        print(f"{difference:.2f}")

if __name__ == "__main__":
    main()
