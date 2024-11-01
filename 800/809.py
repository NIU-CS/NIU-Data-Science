# 809

import re

def is_valid_password(password):
    if len(password) < 8:
        return False
    if not re.match(r'^[A-Za-z0-9]+$', password):
        return False
    if not re.search(r'[A-Z]', password):
        return False
    return True

def main():
    password = input()

    if is_valid_password(password):
        print("Valid password")
    else:
        print("Invalid password")

if __name__ == "__main__":
    main()
