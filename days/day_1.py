# -*- coding: utf-8 -*-

from itertools import combinations
from numpy import sum

from .abstract_day import AbstractDay
from .utils import read_ints, product


class Day1(AbstractDay):
    TARGET_VALUE: int = 2020

    def partOne(self) -> int:
        return Day1._calculate(self.inputs_path, 2)

    def partTwo(self) -> int:
        return Day1._calculate(self.inputs_path, 3)

    @staticmethod
    def _calculate(file_path: str, entry_count: int) -> int:
        for comb in combinations(read_ints(file_path), entry_count):
            if sum(comb) == Day1.TARGET_VALUE:
                return product(comb)
