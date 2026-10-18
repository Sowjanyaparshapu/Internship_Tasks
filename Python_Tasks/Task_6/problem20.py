# Validating phone numbers
# problem link - https://www.hackerrank.com/challenges/validating-the-phone-number/problem


import re

def check_mobile_number(number):
    if re.fullmatch(r'[789][0-9]{9}', number):
        print("YES")
    else:
        print("NO")


def main():
    n = int(input())

    for i in range(n):
        number = input()
        check_mobile_number(number)


if __name__ == '__main__':
    main()
