# -*- coding: utf-8 -*-

from itertools import combinations
from numpy import sum

from .abstract_day import AbstractDay
from .utils import read_ints, read_lines, product


class Day0(AbstractDay):
    def partOne(self) -> int:
        result: int = 0

        for line in read_lines(self.inputs_path):
            if line:
                pass
            else:
                pass
        else:
            pass

        return result

    def partTwo(self) -> int:
        result: int = 0
        for value in read_ints(self.inputs_path):
            pass
        return result
