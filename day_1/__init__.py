from itertools import combinations


def day_1_1():
    lines = []
    with open("day_1/data.txt") as f:
        lines = f.readlines()[:-1]
    for x, y in combinations(lines, 2):
        if int(x) + int(y) == 2020:
            print(int(x) * int(y))
    # [print(int(x)*int(y)) for x, y in combinations(open("day_1/data.txt").readlines()[:-1], 2) if int(x)+int(y) == 2020]


def day_1_2():
    lines = []
    with open("day_1/data.txt") as f:
        lines = f.readlines()[:-1]
    for x, y, z in combinations(lines, 3):
        if int(x) + int(y) + int(z) == 2020:
            print(int(x) * int(y) * int(z))
    # [print(int(x)*int(y)*int(z)) for x, y, z in combinations(open("day_1/data.txt").readlines()[:-1], 3) if int(x)+int(y) == 2020]
