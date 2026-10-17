# Introduction to sets
# problem link - https://www.hackerrank.com/challenges/py-introduction-to-sets/problem

def average(array):
    array=set(array)
    total_sum=0
    total_numbers=0
    for i in array:
        total_sum=total_sum+i
        total_numbers+=1
    avg=total_sum/total_numbers
    return round(avg,3)
        
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
