# -*- coding: utf-8 -*-

from typing import Tuple

from .abstract_day import AbstractDay
from .utils import read_lines


class Day2(AbstractDay):
    def partOne(self) -> int:
        cumm: int = 0
        for line in read_lines(self.inputs_path):
            (a, b), char, string = Day2.parse_line(line)
            cumm += (a <= string.count(char) <= b)
        return cumm

    def partTwo(self) -> int:
        cumm: int = 0
        for line in read_lines(self.inputs_path):
            (a, b), char, string = Day2.parse_line(line)
            cumm += ((string[a - 1] == char) ^ (string[b - 1] == char))
        return cumm

    @staticmethod
    def parse_line(line: str) -> Tuple[Tuple[int, int], str, str]:
        r, char_cond, string = line.split(" ")
        a, b = [int(val) for val in r.split("-")][:2]
        char = char_cond[0]
        return (a, b), char, string
