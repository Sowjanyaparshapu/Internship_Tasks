# set.union()
#problem link - https://www.hackerrank.com/challenges/py-set-union/problem


def newspaper_subscriptions(n, english, m, french):
    result = english.union(french)
    print(len(result))


def main():
    n = int(input())
    english = set(map(int, input().split()))

    m = int(input())
    french = set(map(int, input().split()))

    newspaper_subscriptions(n, english, m, french)


if __name__ == '__main__':
    main()
