from itertools import combinations
import numpy as np


def day_1_1():
    lines = []
    with open("day_1/data.txt") as f:
        lines = [int(i) for i in f.readlines()[:-1]]
    for comb in combinations(lines, 2):
        if np.sum(comb) == 2020:
            print(np.prod(comb))
    # [print(np.prod(comb)) for comb in combinations([int(i) for i in open("day_1/data.txt").readlines()[:-1]], 2) if np.sum(prod) == 2020]


def day_1_2():
    lines = []
    with open("day_1/data.txt") as f:
        lines = [int(i) for i in f.readlines()[:-1]]
    for comb in combinations(lines, 3):
        if np.sum(comb) == 2020:
            print(np.prod(comb))
    # [print(np.prod(comb)) for comb in combinations([int(i) for i in open("day_1/data.txt").readlines()[:-1]], 3) if np.sum(prod) == 2020]
