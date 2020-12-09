# -*- coding: utf-8 -*-

from .abstract_day import AbstractDay
from .utils import read_lines


class Day7(AbstractDay):
    def partOne(self) -> int:
        # Parse data in structure
        bags = {}
        for ll in read_lines(self.inputs_path):
            a, b = ll.split(" bags contain ")

            if "no" in b:
                bags[a] = {}
            else:
                contents = {}
                for c in b.strip().split(", "):
                    cc = c.split(" ")
                    if cc[0] != "no":
                        count = int(cc[0])
                        color = " ".join(cc[1:-1])
                        contents[color] = count

                bags[a] = contents

        bag_colors = list(bags.keys())
        contains = [c for c in bag_colors if "shiny gold" in bags[c]]

        last_size, current_size = 0, len(contains)
        while current_size != last_size:  # not reached stable state
            last_size = current_size

            for c in bag_colors:
                if c not in contains:
                    for cc in bags[c]:
                        if cc in contains:
                            contains.append(c)
                            break

            current_size = len(contains)

        return current_size

    def partTwo(self) -> None:
        return None

