# -*- coding: utf-8 -*-

import numpy as np
from typing import List, Tuple

from .abstract_day import AbstractDay
from .utils import read_lines

int64 = np.int64
uint64 = np.uint64


class Day13(AbstractDay):
    def partOne(self) -> uint64:
        target_value, divisors = Day13.parseForPartOne(self.inputs_path)

        closest_divisor: uint64 = divisors.pop(0)
        least_distance: uint64 = closest_divisor - (target_value % closest_divisor)

        for divisor in divisors:
            distance: uint64 = divisor - (target_value % divisor)
            if distance < least_distance:
                closest_divisor = divisor
                least_distance = distance

        # print(f"{closest_divisor=} {least_distance=}")

        return closest_divisor * least_distance

    @staticmethod
    def parseForPartOne(file_path: str) -> Tuple[uint64, List[uint64]]:
        lines = read_lines(file_path)
        target_value = uint64(lines[0])
        values = [uint64(e) for e in lines[1].split(",") if e != "x"]
        return target_value, values

    def partTwo(self) -> int64:
        entries: List[Tuple[int64, int64]] = Day13.parseForPartTwo(self.inputs_path)  # List[(divisor, remainder)]

        step_counter = np.uint64(0)
        cummul_divisor, cummul_remainder = entries.pop(-1)
        while entries:
            n_divisor, n_remainder = cummul_divisor, cummul_remainder
            m_divisor, m_remainder = entries.pop(-1)

            diff_remainder_n_m = np.int64(n_remainder - m_remainder)

            n_candidate = int64(0)
            while n_candidate < n_divisor:  # On average, faster than a ranged loop
                if int64((diff_remainder_n_m + n_candidate * n_divisor) % m_divisor) == 0:
                    break
                n_candidate += 1

            net_remainder = np.int64(n_remainder + n_candidate * n_divisor)
            net_divisor = np.int64(n_divisor * m_divisor)

            cummul_divisor, cummul_remainder = (net_divisor, net_remainder)

            step_counter += n_candidate

        # print(f"{step_counter=}")

        return cummul_remainder

    @staticmethod
    def parseForPartTwo(file_path: str) -> List[Tuple[int64, int64]]:
        """
        Returns pairs (divisor, remainder) for each entry in file
        """
        raw_entries: List[str] = (read_lines(file_path)[1]).split(",")
        return sorted(
            [(int64(number), int64(-bus_id)) for bus_id, number in enumerate(raw_entries) if number != "x"],
            key=lambda entry: entry[0]  # Sorted ascendingly by divisor
        )
