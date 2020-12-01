from itertools import combinations
import numpy as np
from typing import List


def ints_from_file(file_path) -> List[int]:
    ints = []
    with open("day_1/data.txt") as f:
        for line in f:
            try:
                i = int(line)
                ints.append(i)
            except:
                pass
    return ints


def day_1_1():
    for comb in combinations(ints_from_file("day_1/data.txt"), 2):
        if np.sum(comb) == 2020:
            print(np.prod(comb))
    # [print([np.prod(comb) for comb in combinations([int(i) for i in open("day_1/data.txt").readlines()[:-1]], 2) if np.sum(comb) == 2020])]


def day_1_2():
    for comb in combinations(ints_from_file("day_1/data.txt"), 3):
        if np.sum(comb) == 2020:
            print(np.prod(comb))
    # [print([np.prod(comb) for comb in combinations([int(i) for i in open("day_1/data.txt").readlines()[:-1]], 3) if np.sum(comb) == 2020])]
