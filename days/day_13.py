# -*- coding: utf-8 -*-

from itertools import combinations
import numpy as np
import numba

from .abstract_day import AbstractDay
from .utils import read_ints, read_lines, product


class Day13(AbstractDay):
    def partOne(self) -> int:
        lines = read_lines(self.inputs_path)
        target_t = int(lines[0])
        tt = [int(i) for i in lines[1].split(",") if i != "x"]

        closest, closest_distance = -1, 10000

        for t in tt:
            ta = ((target_t // t) + 1) * t
            dist = ta - target_t
            if dist < closest_distance:
                closest = t
                closest_distance = dist

        return closest * closest_distance

    def partTwo(self) -> int:
        values = []
        skips = []
        lines = read_lines(self.inputs_path)

        for vv in lines[1].split(","):
            if vv == "x":
                skips[-1] += 1
            else:
                values.append(int(vv))
                skips.append(1)

        if skips[-1] != 0:
            skips[-1] = 0
        print(f"{skips=}")
        print(
f"""
#include <iostream>
#include <cstdint>

int main() {{
\tuint64_t target{{{values[0]}}};
\tfor (uint64_t i{{ target }}; i < 18446744073709551615-target+1ull; i += target) {{
"""
        )

        string = "i"
        tab = '\t'
        for i, (v, s) in enumerate(zip(values[1:], skips[:-1])):
            string += f" + {s}"
            print(f"{tab*(i+2)}if ((({string}) % {v}) == 0) {{")

        print(f"{tab * (len(values) + 1)}std::cout << i << std::endl;")
        print(f"{tab * (len(values) + 1)}break;")

        for i in range(len(values)-1)[::-1]:
            print(f"{tab * (i + 2)}}}")
        print("\t}")

        print("\tstd::cin.get();")
        print("}")
