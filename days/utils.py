from datetime import datetime
from typing import Iterable, List
import numpy as np


def int_to_bin_str(i: int, bit_width: int = -1) -> str:
    binary_str: str = bin(i)[2:]  # remove '0b' prefix

    len_binary_str: int = len(binary_str)
    if len_binary_str < bit_width:
        left_padding: str = "0" * (bit_width - len_binary_str)
        binary_str: str = left_padding + binary_str

    return binary_str


def product(iterable: Iterable[int]) -> int:
    cummul: int = 1
    for value in iterable:
        cummul *= value
    return cummul


def read_ints(file_path: str) -> np.ndarray:
    """ Presumes 1 int per line """
    with open(file_path, encoding="utf-8") as f:
        return np.array([int(line.strip()) for line in f.readlines() if line], dtype=np.int64)


def read_lines(file_path: str, stripped: bool = True) -> List[str]:
    with open(file_path, encoding="utf-8") as f:
        return [line.strip() for line in f.readlines() if line] if stripped \
            else [line for line in f.readlines() if line]


def read_text_as_binary(file_path: str, true_char: str) -> np.ndarray:
    """ Presumes 1 int per line """
    with open(file_path, encoding="utf-8") as f:
        return np.array([[1 if c == true_char else 0 for c in line.strip()] for line in f.readlines()],
                        dtype=np.uint8)


def timeExec(f):
    t1 = datetime.now()
    result = f()
    t2 = datetime.now()
    return (t2 - t1).total_seconds(), result
