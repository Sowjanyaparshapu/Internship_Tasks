# Alphabet Rangoli
# problem link - https://www.hackerrank.com/challenges/alphabet-rangoli/problem

def print_rangoli(size):
    import string
    alphabet = string.ascii_lowercase

    lines = []

    for i in range(size):
        letters = alphabet[size - 1:size - i - 1:-1]
        row = list(letters + alphabet[size - i - 1:size])
        pattern = "-".join(row)
        lines.append(pattern.center(4 * size - 3, "-"))

    for i in range(size - 2, -1, -1):
        lines.append(lines[i])

    print("\n".join(lines))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
