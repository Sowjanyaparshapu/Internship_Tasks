# Designer Door Mat
# problem link - https://www.hackerrank.com/challenges/designer-door-mat/problem

def main():
    n, m = map(int, input().split())

    for i in range(1, n, 2):
        pattern = '.|.' * i
        print(pattern.center(m, '-'))

    print('WELCOME'.center(m, '-'))

    for i in range(n - 2, 0, -2):
        pattern = '.|.' * i
        print(pattern.center(m, '-'))


if __name__ == '__main__':
    main()
