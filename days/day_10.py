# -*- coding: utf-8 -*-

from itertools import combinations
import numpy as np

from .abstract_day import AbstractDay
from .utils import read_ints, read_lines, product


class Day10(AbstractDay):
    def partOne(self) -> int:
        devices = sorted(list(read_ints(self.inputs_path)))
        built_in = np.max(devices) + 3

        devices = [0] + devices + [built_in]

        difference_counts = [0, 0, 0]

        vin = devices.pop(0)
        while devices:
            for i in range(3):
                if vin + i + 1 in devices:
                    difference_counts[i] += 1
                    vin = devices.pop(devices.index(vin + i + 1))
                    break

        count_1_jolt_difference = difference_counts[0]
        count_3_jolt_difference = difference_counts[2]

        return count_1_jolt_difference * count_3_jolt_difference

    def partTwo(self) -> int:
        devices = sorted(list(read_ints(self.inputs_path)))
        built_in = np.max(devices) + 3

        devices = devices + [built_in]
        known_paths = {}

        def solve(prev, l_devices):
            if len(l_devices) == 1:
                return 1
            elif prev in known_paths:
                return known_paths[prev]
            else:
                result = np.sum([solve(val, l_devices[l_devices.index(val):]) for val in range(prev + 1, prev + 3 + 1) if val in l_devices], dtype=np.uint64)
                known_paths[prev] = result
                return result
                # cumm = 0
                # for val in range(prev + 1, prev + 3 + 1):
                #     if val in l_devices:
                #         count = solve(val, l_devices[l_devices.index(val):])
                #         cumm += count
                # return cumm

        return solve(0, devices)
