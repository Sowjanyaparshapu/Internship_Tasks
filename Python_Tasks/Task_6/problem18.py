# Set Mutation
# problem link - https://www.hackerrank.com/challenges/py-set-mutations/problem


def modify_set(a, operations):
    for operation, other_set in operations:
        if operation == "update":
            a.update(other_set)
        elif operation == "intersection_update":
            a.intersection_update(other_set)
        elif operation == "difference_update":
            a.difference_update(other_set)
        elif operation == "symmetric_difference_update":
            a.symmetric_difference_update(other_set)

    print(sum(a))


def main():
    n = int(input())
    a = set(map(int, input().split()))

    m = int(input())
    operations = []

    for i in range(m):
        operation, length = input().split()
        other_set = set(map(int, input().split()))
        operations.append((operation, other_set))

    modify_set(a, operations)


if __name__ == '__main__':
    main()
