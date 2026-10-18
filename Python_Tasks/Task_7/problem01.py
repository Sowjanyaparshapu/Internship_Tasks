3 set.symmetric difference
# problem link - https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem


def calculate(n, english, m, french):
    result = english.symmetric_difference(french)
    print(len(result))


def main():
    n = int(input())
    english = set(map(int, input().split()))

    m = int(input())
    french = set(map(int, input().split()))

    calculate(n, english, m, french)


if __name__ == '__main__':
    main()
