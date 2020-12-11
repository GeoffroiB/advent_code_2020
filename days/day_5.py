# -*- coding: utf-8 -*-

import numpy as np

from .abstract_day import AbstractDay
from .utils import read_lines


class Day5(AbstractDay):
    def partOne(self) -> int:
        map_letters_row = {"B": "1", "F": "0"}
        map_letters_col = {"R": "1", "L": "0"}

        highest_id = 0
        for line in read_lines(self.inputs_path):
            bin_row = "".join([map_letters_row[c] for c in line[:7]])
            bin_column = "".join([map_letters_col[c] for c in line[7:]])

            row, column = int(bin_row, 2), int(bin_column, 2)
            i = row * 8 + column

            highest_id = i if i > highest_id else highest_id

        return highest_id

    def partTwo(self) -> int:
        map_letters_row = {"B": "1", "F": "0"}
        map_letters_col = {"R": "1", "L": "0"}
        possibilities = list(range(int("1111111111", 2) + 1))

        for line in read_lines(self.inputs_path):
            bin_row = "".join([map_letters_row[c] for c in line[:7]])
            bin_column = "".join([map_letters_col[c] for c in line[7:]])

            row, column = int(bin_row, 2), int(bin_column, 2)
            i = row * 8 + column

            possibilities[i] = -1

        min_id, max_id = int("1000000000", 2), int("1111111000", 2)

        for i in possibilities:
            if i != -1:  # Remove used seats
                if min_id <= i < max_id:  # "Your seat wasn't at the very front or back"
                    if i-1 not in possibilities:  # Previous seat not in list
                        if i+1 not in possibilities:  # Next seat not in list
                            return i

        return -1  # Not found
