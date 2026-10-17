# collections.counter
# problem link - https://www.hackerrank.com/challenges/collections-counter/problem

from collections import Counter
n = int(input())
shoe_sizes = list(map(int, input().split()))
shoe_count = Counter(shoe_sizes)
customers = int(input())
money = 0
for i in range(customers):
    size, price = map(int, input().split())
    if shoe_count[size] > 0:
        money = money + price
        shoe_count[size] = shoe_count[size] - 1
print(money)
