# -*- coding: utf-8 -*-

import numpy as np
from typing import Dict, List, Tuple

from .abstract_day import AbstractDay
from .utils import int_to_bin_str, read_lines


class Day15(AbstractDay):
    def partOne(self) -> np.uint64:
        line = read_lines(self.inputs_path)[0]

        numbers = [int(n) for n in line.split(",")]
        numbers_coll = {n: i for i, n in enumerate(numbers)}

        last_value = numbers[-1]
        for i in range(len(numbers) - 1, 2020 - 1):
            diff = 0
            if last_value in numbers_coll:
                diff = i - numbers_coll[last_value]

            numbers_coll[last_value] = i
            last_value = diff

        return last_value

    def partTwo(self) -> np.uint64:
        line = read_lines(self.inputs_path)[0]

        numbers = [int(n) for n in line.split(",")]
        numbers_coll = {n: i for i, n in enumerate(numbers)}

        last_value = numbers[-1]
        for i in range(len(numbers) - 1, 30000000 - 1):
            diff = 0
            if last_value in numbers_coll:
                diff = i - numbers_coll[last_value]

            numbers_coll[last_value] = i
            last_value = diff

        return last_value
