# -*- coding: utf-8 -*-

import numpy as np
from typing import List, Tuple

from .abstract_day import AbstractDay
from .utils import product, read_text_as_binary


class Day3(AbstractDay):
    OBSTACLE_CHAR = "#"

    def partOne(self) -> int:
        bin_matrix: np.ndarray = read_text_as_binary(self.inputs_path, Day3.OBSTACLE_CHAR)
        return Day3.count_collisions(bin_matrix, dx=3, dy=1)

    def partTwo(self) -> int:
        slopes: List[Tuple[int, int]] = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

        bin_matrix: np.ndarray = read_text_as_binary(self.inputs_path, Day3.OBSTACLE_CHAR)
        collision_counts: List[int] = [Day3.count_collisions(bin_matrix, dx, dy) for dx, dy in slopes]

        return product(collision_counts)

    @staticmethod
    def count_collisions(bin_matrix: np.ndarray, dx: int, dy: int) -> int:
        row_length = bin_matrix.shape[1]

        collision_count, x, y = 0, 0, 0
        for row_index, row in enumerate(bin_matrix):
            if row_index != y:
                continue

            if row[x]:
                collision_count += 1

            x = (x + dx) % row_length
            y += dy

        return collision_count
