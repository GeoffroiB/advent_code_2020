# -*- coding: utf-8 -*-

import numpy as np
from typing import Dict, List, Tuple

from .abstract_day import AbstractDay
from .utils import int_to_bin_str, read_lines


class Day14(AbstractDay):
    def partOne(self) -> np.uint64:
        memory: Dict[int, int] = {}
        mask: str = "X" * 36

        for line in read_lines(self.inputs_path):
            if "mem" in line:
                # Parse entry
                parsed_addr, parsed_value = Day14.parseMemLine(line)

                # Apply mask to value
                value_bits: List[str] = list(int_to_bin_str(parsed_value, bit_width=36))
                for i, m in enumerate(mask):
                    if m != "X":
                        value_bits[i]: str = m

                # Store value
                memory[parsed_addr]: int = int("".join(value_bits), 2)

            elif "mask" in line:
                mask: str = Day14.parseMaskLine(line)

        return np.uint64(np.sum([v for v in memory.values()], dtype=np.uint64))

    def partTwo(self) -> np.uint64:
        memory: Dict[int, int] = {}
        mask: str = "X" * 36

        for line in read_lines(self.inputs_path):
            if "mem" in line:
                # Parse entry
                parsed_addr, parsed_value = Day14.parseMemLine(line)
                addresses: List[int] = Day14.getAllAddresses(mask, parsed_addr)

                for addr in addresses:
                    memory[addr]: int = parsed_value

            elif "mask" in line:
                mask: str = Day14.parseMaskLine(line)

        return np.uint64(np.sum([v for v in memory.values()], dtype=np.uint64))

    @staticmethod
    def parseMaskLine(line: str) -> str:
        mask_start_index: int = line.index("=") + 1
        mask: str = line[mask_start_index:].strip()[:36]
        return mask

    @staticmethod
    def parseMemLine(line: str) -> Tuple[int, int]:
        addr: int = int(line[line.index("[") + 1:line.index("]")])
        value: int = int(line[line.index("=") + 1:].strip(), 10)
        return addr, value

    @staticmethod
    def getAllAddresses(floating_mask: str, address: int) -> List[int]:
        address_string: str = int_to_bin_str(address, bit_width=len(floating_mask))

        # Apply mask replacements to address_string
        partially_masked_address: List[str] = [a if m == "0" else m for a, m in zip(address_string, floating_mask)]

        # Generate all adresses considering floating bits
        addresses: List[str] = []
        for a, m in zip(partially_masked_address[1:], floating_mask[1:]):
            if m == "X":
                addresses: List[str] = \
                    [addr + "0" for addr in addresses] + [addr + "1" for addr in addresses] if address \
                    else ["0", "1"]
            else:
                addresses: List[str] = [addr + a for addr in addresses] if address else [a]

        result: List[int] = [int(addr, 2) for addr in addresses]
        return result
