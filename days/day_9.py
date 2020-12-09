# -*- coding: utf-8 -*-
import numpy as np
from itertools import combinations
from typing import List, Optional

from .abstract_day import AbstractDay
from .utils import read_ints


class Day9(AbstractDay):
    def partOne(self) -> Optional[int]:
        values = read_ints(self.inputs_path)
        return Day9._calcPartOne(values)

    def partTwo(self) -> Optional[int]:
        values: List[int] = read_ints(self.inputs_path)
        length_values: int = len(values)

        result_part_one: int = Day9._calcPartOne(values)

        for length_sub_values in range(2, length_values):  # All possible group lengths
            for a in range(length_values - length_sub_values):  # All start index possible for groups of length
                b: int = a+length_sub_values

                if np.sum(values[a:b]) == result_part_one:
                    sub_values = values[a:b]
                    return np.min(sub_values) + np.max(sub_values)

        return None

    @staticmethod
    def _calcPartOne(values: List[int]) -> Optional[int]:
        length_values: int = len(values)
        preamble: int = 25

        for b in range(preamble, length_values):
            for x, y in combinations(values[b-preamble:b], 2):
                if x + y == values[b]:
                    break
            else:
                return int(values[b])

        return None
