# -*- coding: utf-8 -*-

import numpy as np
from string import ascii_lowercase
from typing import List

from .abstract_day import AbstractDay
from .utils import read_lines


class Day6(AbstractDay):
    def partOne(self) -> int:
        total: int = 0

        group_answers = ""
        for line in read_lines(self.inputs_path):
            if line:
                group_answers += line.strip()
            elif group_answers:
                total += len([char for char in set(group_answers) if char in ascii_lowercase])
                group_answers = ""
        else:
            total += len([char for char in set(group_answers) if char in ascii_lowercase])

        return total

    def partTwo(self) -> int:
        total: int = 0

        group_answers = []
        for line in read_lines(self.inputs_path):
            if line:
                group_answers.append(set(line.strip()))
            elif group_answers:
                group_intersection = group_answers[0]

                for answer in group_answers[1:]:
                    group_intersection.intersection_update(answer)

                total += len(group_intersection)
                group_answers = []

        return total
