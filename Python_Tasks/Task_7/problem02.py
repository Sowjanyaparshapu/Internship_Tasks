# Captains Room
# problem link - https://www.hackerrank.com/challenges/py-the-captains-room/problem


def find_captain_room(k, rooms):
    unique_rooms = set(rooms)

    captain_room = (k * sum(unique_rooms) - sum(rooms)) // (k - 1)

    print(captain_room)


def main():
    k = int(input())
    rooms = list(map(int, input().split()))

    find_captain_room(k, rooms)


if __name__ == '__main__':
    main()
