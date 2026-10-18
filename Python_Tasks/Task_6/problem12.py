# set. discard(),pop(),remove()
# problem link - https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem


def modify_set(n, s, commands):
    for i in range(commands):
        operation = input().split()

        if operation[0] == "pop":
            s.remove(min(s))
        elif operation[0] == "remove":
            s.discard(int(operation[1]))
        elif operation[0] == "discard":
            s.discard(int(operation[1]))

    print(sum(s))


if __name__ == '__main__':
    n = int(input())
    s = set(map(int, input().split()))
    commands = int(input())

    modify_set(n, s, commands)

