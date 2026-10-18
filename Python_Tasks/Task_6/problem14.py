# set.intersection()
# problem link - https://www.hackerrank.com/challenges/py-set-intersection-operation/problem


def newspaper_subscriptions(n, english, m, french):
    result = english.intersection(french)
    print(len(result))


def main():
    n = int(input())
    english = set(map(int, input().split()))

    m = int(input())
    french = set(map(int, input().split()))

    newspaper_subscriptions(n, english, m, french)


if __name__ == '__main__':
    main()
