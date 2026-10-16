# Consecutive Numbers printing
# Problem line - https://www.hackerrank.com/challenges/python-print/problem

def consecutives(n):
    for i in range(1,n+1):
        print(i,end="")
if __name__ == '__main__':
    n = int(input())
    consecutives(n)
