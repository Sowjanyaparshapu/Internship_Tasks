# set.add()
# problem link- https://www.hackerrank.com/challenges/py-set-add/problem


n = int(input())
country_names = []
for i in range(n):
    country = input()
    country_names.append(country)
country_unique_names = set(country_names)
count = 0
for i in country_unique_names:
    count = count + 1
print(count)
