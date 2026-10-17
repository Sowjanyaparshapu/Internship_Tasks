# Piling up
# probelm link - https://www.hackerrank.com/challenges/piling-up/problem


def piling_up(blocks):
    left = 0
    right = len(blocks) - 1
    top = float('inf')

    while left <= right:
        if blocks[left] >= blocks[right]:
            bigger = blocks[left]
        else:
            bigger = blocks[right]

        if bigger > top:
            return "No"

        top = bigger

        if blocks[left] >= blocks[right]:
            left += 1
        else:
            right -= 1

    return "Yes"


if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        n = int(input())
        blocks = list(map(int, input().split()))

        result = piling_up(blocks)
        print(result)
