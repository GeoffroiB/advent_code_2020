# -*- coding: utf-8 -*-

import numpy as np
from typing import Optional

from .abstract_day import AbstractDay
from .utils import read_lines


class Day5(AbstractDay):
    def partOne(self) -> int:
        highest_seat_id = 0

        for line in read_lines(self.inputs_path):
            seat_id = Day5.stringToSeatID(line)
            highest_seat_id = seat_id if seat_id > highest_seat_id else highest_seat_id

        return highest_seat_id

    def partTwo(self) -> Optional[int]:
        total_seat_count = int("1111111111", 2) + 1
        min_id, max_id = int("1000000000", 2), int("1111111000", 2)

        possibilities = np.arange(total_seat_count, dtype=int)

        for line in read_lines(self.inputs_path):
            seat_id = Day5.stringToSeatID(line)
            possibilities[seat_id] = -1

        for seat_id in possibilities:
            if min_id <= seat_id < max_id:
                """
                "Your seat wasn't at the very front or back"
                but also ignores used seats -> -1
                """
                if seat_id - 1 not in possibilities:  # Previous seat not in list
                    if seat_id + 1 not in possibilities:  # Next seat not in list
                        return seat_id

        return None  # Not found

    @staticmethod
    def stringToSeatID(string: str) -> int:
        seat_id = 0
        for c in string:
            seat_id *= 2
            if c == "B" or c == "R":
                seat_id += 1
        return seat_id
