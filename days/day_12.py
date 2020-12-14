# -*- coding: utf-8 -*-

from itertools import combinations
import numpy as np

from .abstract_day import AbstractDay
from .utils import read_ints, read_lines, product

# Basic template for new day (Copy Pasta base)
class Day12(AbstractDay):
    def partOne(self) -> int:
        result: int = 0

        x, y = 0, 0
        dx, dy = 1, 0

        for line in read_lines(self.inputs_path):
            direction = line[0]
            step_length = int(line[1:])

            if direction == "N":
                y += step_length
            elif direction == "S":
                y -= step_length
            elif direction == "E":
                x += step_length
            elif direction == "W":
                x -= step_length
            else:
                if direction == "L":
                    for i in range(step_length // 2):
                        dx, dy = -dy, dx

                elif direction == "R":
                    for i in range(step_length // 2):
                        dx, dy = dy, -dx

                elif direction == "F":
                    x += step_length * dx
                    y += step_length * dy

            # print(f"{dx=} {dy=} {step_length=} \n {x=} {y=} \n")

        return np.abs(x) + np.abs(y)

    def partTwo(self) -> int:
        result: int = 0

        wx, wy = 10, 1
        x, y = 0, 0
        dx, dy = 1, 0

        for line in read_lines(self.inputs_path):
            direction = line[0]
            step_length = int(line[1:])

            if direction == "N":
                wy += step_length
            elif direction == "S":
                wy -= step_length
            elif direction == "E":
                wx += step_length
            elif direction == "W":
                wx -= step_length
            else:
                if direction == "L":
                    # wx -= x
                    # wy -= y
                    for i in range(step_length // 90):
                        wx, wy = -wy, wx
                    # wx += x
                    # wy += y

                elif direction == "R":
                    # wx -= x
                    # wy -= y
                    for _ in range(step_length // 90):
                        wx, wy = wy, -wx
                    # wx += x
                    # wy += y

                elif direction == "F":
                    ddx, ddy = (wx - x), (wy - y)
                    for _ in range(step_length):

                        x += wx
                        y += wy


            # print(f"{direction} {step_length=} \n{wx=} {wy=}\n{x=} {y=} \n")

        return np.abs(x) + np.abs(y)
