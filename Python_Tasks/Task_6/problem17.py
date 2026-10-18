# Check strict superset
# problem link - https://www.hackerrank.com/challenges/py-check-strict-superset/problem


def check_superset(a, other_sets):
    for s in other_sets:
        if not a.issuperset(s) or a == s:
            print("False")
            return

    print("True")


def main():
    a = set(map(int, input().split()))
    n = int(input())

    other_sets = []

    for i in range(n):
        s = set(map(int, input().split()))
        other_sets.append(s)

    check_superset(a, other_sets)


if __name__ == '__main__':
    main()
