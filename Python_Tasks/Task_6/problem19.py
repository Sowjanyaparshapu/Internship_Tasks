# company logo
# program link - https://www.hackerrank.com/challenges/most-commons/problem


def most_common_characters(s):
    frequency = {}

    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    result = sorted(frequency.items(), key=lambda x: (-x[1], x[0]))

    for char, count in result[:3]:
        print(char, count)


def main():
    s = input()
    most_common_characters(s)


if __name__ == '__main__':
    main()
