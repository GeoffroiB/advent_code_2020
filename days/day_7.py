# -*- coding: utf-8 -*-

import numpy as np

from .abstract_day import AbstractDay
from .utils import read_lines


class Day7(AbstractDay):
    def partOne(self) -> int:
        # Parse data in structure
        bag_contents = {}

        for ll in read_lines(self.inputs_path):
            color, contents_string = ll.split(" bags contain ")

            bag_contents[color] = {}
            if "no" not in contents_string:
                for item in contents_string.strip().split(", "):
                    item_qt, *item_color = item.split(" ")

                    item_qt = int(item_qt)
                    item_color = " ".join(item_color[:-1])

                    bag_contents[color][item_color] = item_qt

        solveds = {}

        def solve(c) -> bool:
            if c not in solveds:  # Not already solved
                for sub_c in bag_contents[c]:
                    if sub_c == "shiny gold" or solve(sub_c):
                        solveds[c] = True
                        break
                else:
                    solveds[c] = False

            return solveds[c]

        result: int = np.count_nonzero([solve(bag_c) for bag_c in bag_contents])

        return result

    def partTwo(self) -> None:
        return None

