# Finding Second max element
# program link - https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem


def sec_max(n, arr):
    first_max = arr[0]
    for i in range(len(arr)):
        if arr[i] > first_max:
            first_max = arr[i]
    second_max = None
    for i in range(len(arr)):
        if arr[i] < first_max:
            if second_max is None or arr[i] > second_max:
                second_max = arr[i]
    print(second_max)
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    sec_max(n, arr)
