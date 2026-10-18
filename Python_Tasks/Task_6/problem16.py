# Checking subset
# problem link - https://www.hackerrank.com/challenges/py-check-subset/problem


def check_subset(a, b):
    if a.issubset(b):
        print("True")
    else:
        print("False")


def main():
    t = int(input())

    for i in range(t):
        n = int(input())
        a = set(map(int, input().split()))

        m = int(input())
        b = set(map(int, input().split()))

        check_subset(a, b)


if __name__ == '__main__':
    main()
