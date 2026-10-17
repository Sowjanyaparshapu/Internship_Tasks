# swapped string
# problem link - https://www.hackerrank.com/challenges/swap-case/problem


def swap_case(s):
    swaped_str = ""

    for ch in s:
        if ch.isupper():
            swaped_str += ch.lower()
        elif ch.islower():
            swaped_str += ch.upper()
        else:
            swaped_str += ch

    return swaped_str



if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
