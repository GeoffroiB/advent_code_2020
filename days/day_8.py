# -*- coding: utf-8 -*-
from copy import deepcopy

from .abstract_day import AbstractDay
from .utils import read_lines


class Day8(AbstractDay):
    def partOne(self) -> int:
        data_lines = read_lines(self.inputs_path)
        acc = 0
        line_count = len(data_lines)
        line_index = 0
        executed = []

        while line_index < line_count:
            line = data_lines[line_index]
            op, arg = line.split(" ")

            if (line_index + 0) in executed:
                break

            if op == "nop":
                line_index += 1
                executed.append(line_index - 1)
            else:
                value = int(arg[1:]) if arg[0] == "+" else -int(arg[1:])

                if op == "acc":
                    acc += value
                    line_index += 1
                    executed.append(line_index - 1)
                elif op == "jmp":
                    line_index += value
                    executed.append(line_index - value)

        return acc

    def partTwo(self) -> int:
        data_lines = read_lines(self.inputs_path)
        line_count = len(data_lines)

        for i in range(line_count):
            acc = 0

            lines = deepcopy(data_lines)
            if "jmp" in lines[i]:
                lines[i] = "nop " + lines[i][4:]
            elif "nop" in lines[i]:
                lines[i] = "jmp " + lines[i][4:]
            else:
                continue

            line_index = 0
            executed = []

            while line_index < line_count:
                line = lines[line_index]
                op, arg = line.split(" ")

                if line_index in executed:
                    break

                if op == "nop":
                    line_index += 1
                    executed.append(line_index - 1)
                else:
                    value = int(arg[1:]) if arg[0] == "+" else -int(arg[1:])

                    if op == "acc":
                        acc += value
                        line_index += 1
                        executed.append(line_index - 1)

                    elif op == "jmp":
                        line_index += value
                        executed.append(line_index - value)
            else:
                return acc

        return -1
