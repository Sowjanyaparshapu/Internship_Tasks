# string validators
# problem link - https://www.hackerrank.com/challenges/string-validators/problem


def string_validators(s):
    if any(i.isalnum() for i in s):
        print("True")
    else:
        print("False")

    if any(i.isalpha() for i in s):
        print("True")
    else:
        print("False")

    if any(i.isdigit() for i in s):
        print("True")
    else:
        print("False")

    if any(i.islower() for i in s):
        print("True")
    else:
        print("False")

    if any(i.isupper() for i in s):
        print("True")
    else:
        print("False")


if __name__ == '__main__':
    s = input()
    string_validators(s)
