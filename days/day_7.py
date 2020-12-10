# -*- coding: utf-8 -*-

import numpy as np
from typing import Dict, List

from .abstract_day import AbstractDay
from .utils import read_lines


class Day7(AbstractDay):
    def partOne(self) -> int:
        # Parse data in structure
        bag_contents = {}

        for line in read_lines(self.inputs_path):
            color, contents = Day7._parse_line(line)
            bag_contents[color] = contents

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

    def partTwo(self) -> np.int64:
        # Parse data in structure
        bag_contents = {}

        for line in read_lines(self.inputs_path):
            color, contents = Day7._parse_line(line)
            bag_contents[color] = contents

        solveds = {}

        def solve(bag_color) -> np.int64:
            if bag_color not in solveds:  # Not already solved
                solveds[bag_color] = np.int64(1) + np.sum(
                    [sub_bag_count * solve(sub_bag_color)
                     for sub_bag_color, sub_bag_count in bag_contents[bag_color].items()]
                    , dtype=np.int64
                )

            return solveds[bag_color]

        count = solve("shiny gold") - 1  # We don't count the 'root' bag

        return count

    @staticmethod
    def _parse_line(line: str) -> (str, Dict[str, int]):
        line = line.strip()[:-1]  # remove '.' at the end of line

        container_color, content_substring = line.split(" bags contain ")[:2]

        if "no" in content_substring:
            return container_color, {}

        contents = {}
        for item_str in content_substring.split(", "):
            index_first_space: int = item_str.index(" ")

            sub_count: int = int(item_str[:index_first_space])

            length_to_exclude: int = len(" bag" if sub_count == 1 else " bags")
            sub_color: str = item_str[index_first_space+1:-length_to_exclude]  # exclude " bags" at the end of item_str

            contents[sub_color] = sub_count

        return container_color, contents
