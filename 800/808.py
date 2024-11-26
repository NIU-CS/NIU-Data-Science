# 808

import re


def main():
    ssn = input()
    pattern = r"^\d{3}-\d{2}-\d{4}$"

    if re.match(pattern, ssn):
        print("Valid SSN")
    else:
        print("Invalid SSN")


if __name__ == "__main__":
    main()
