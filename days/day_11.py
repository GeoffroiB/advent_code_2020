# -*- coding: utf-8 -*-

import numpy as np
from copy import deepcopy

from .abstract_day import AbstractDay
from .utils import read_ints, read_lines, product


class Day11(AbstractDay):
    def partOne(self) -> int:
        state_1 = [[c for c in line] for line in read_lines(self.inputs_path)]
        height, width = len(state_1), len(state_1[0])

        state_2 = [["." for i in range(width)] for j in range(height)]

        def count_around(x, y):
            count = 0
            for a in range(x-1, x+2):
                for b in range(y-1, y+2):
                    if a == x and b == y:
                        continue
                    elif a not in range(height) or b not in range(width):
                        continue
                    count += (state_1[a][b] == "#")
            return count

        while True:
            # print("\n".join(["".join() for row in state_1]), end="\n\n")
            for i, row in enumerate(state_1):
                for j, cell in enumerate(row):
                    n_count = count_around(i, j)

                    if cell == "L" and n_count == 0:
                        state_2[i][j] = "#"
                    elif cell == "#" and n_count >= 4:
                        state_2[i][j] = "L"
                    else:
                        state_2[i][j] = cell

            for r1, r2 in zip(state_1, state_2):
                if "".join(r1) != "".join(r2):
                    break
            else:
                break

            state_1 = deepcopy(state_2)
            # print("\n".join(["".join() for row in state_1]), end="\n\n")

        result = np.sum([np.count_nonzero([c == "#" for c in row]) for row in state_2])

        return result

    def partTwo(self) -> int:
        state_1 = [[c for c in line] for line in read_lines(self.inputs_path)]
        height, width = len(state_1), len(state_1[0])

        state_2 = [["." for i in range(width)] for j in range(height)]

        def count_around(x, y):
            count = 0
            for a in range(x - 1, x + 2):
                for b in range(y - 1, y + 2):
                    if a == x and b == y:
                        continue
                    elif a not in range(height) or b not in range(width):
                        continue
                    elif state_1[a][b] == "#":
                        count += 1
                    elif state_1[a][b] == ".":
                        dx, dy = a-x, b-y  # [-1, 0, 1]
                        a2 = a + dx
                        b2 = b + dy
                        while True:
                            if a2 not in range(height) or b2 not in range(width):
                                break
                            elif state_1[a2][b2] != ".":
                                count += (state_1[a2][b2] == "#")
                                break
                            else:
                                a2 += dx
                                b2 += dy

            return count

        state_2 = deepcopy(state_1)

        while True:
            #print("\n".join(["".join(row) for row in state_1]), end="\n\n")
            for i, row in enumerate(state_1):
                for j, cell in enumerate(row):
                    n_count = count_around(i, j)

                    if cell == ".":
                        continue
                    elif cell == "L":
                        if n_count == 0:
                            state_2[i][j] = "#"
                    elif cell == "#":
                        if n_count >= 5:
                            state_2[i][j] = "L"

            for r1, r2 in zip(state_1, state_2):
                if "".join(r1) != "".join(r2):
                    break
            else:
                break

            state_1 = deepcopy(state_2)
            #print("\n".join(["".join(row) for row in state_1]), end="\n\n")

        result = np.sum([np.count_nonzero([c == "#" for c in row]) for row in state_2])

        return result
