# -*- coding: utf-8 -*-

from .abstract_day import AbstractDay
from .utils import read_ints, read_lines, product


def ishex(s):
    for c in s:
        if c not in "0123456789abcdef":
            return False
    return True


class Day4(AbstractDay):
    VALID_ENTRY_FIELDS = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid'}

    def partOne(self) -> int:
        count = 0
        length_valid_entry_fields = len(Day4.VALID_ENTRY_FIELDS)

        d = {}
        for line in read_lines(self.inputs_path):
            if line:
                for p in line.split(" "):
                    kk = p.split(":")
                    d[kk[0]] = kk[1]

            elif d:
                count_valid_fields = len(Day4.VALID_ENTRY_FIELDS.intersection(set(d.keys())))

                if count_valid_fields == length_valid_entry_fields \
                        or (count_valid_fields == (length_valid_entry_fields - 1) and "cid" not in d):
                    count += 1

                d = {}  # reset
        else:
            if d:
                count_valid_fields = len(Day4.VALID_ENTRY_FIELDS.intersection(set(d.keys())))

                if count_valid_fields == length_valid_entry_fields \
                        or (count_valid_fields == (length_valid_entry_fields - 1) and "cid" not in d):
                    count += 1

        return count

    def partTwo(self) -> int:
        count = 0
        length_valid_entry_fields = len(Day4.VALID_ENTRY_FIELDS)

        d = {}
        for line in read_lines(self.inputs_path):
            if line:
                for p in line.split(" "):
                    kk = p.split(":")
                    d[kk[0]] = kk[1]

            elif d:
                count_valid_fields = len(Day4.VALID_ENTRY_FIELDS.intersection(set(d.keys())))

                if count_valid_fields == length_valid_entry_fields \
                        or (count_valid_fields == (length_valid_entry_fields - 1) and "cid" not in d):
                    if 1920 <= int(d["byr"]) <= 2002 and len(d["byr"]) == 4:
                        if 2010 <= int(d["iyr"]) <= 2020 and len(d["iyr"]) == 4:
                            if len(d["eyr"]) == 4 and d["eyr"].isdigit() and 2020 <= int(d["eyr"]) <= 2030:
                                if d["hcl"].startswith("#") and len(d["hcl"]) == 7 and ishex(d["hcl"][1:]):
                                    if len(d["pid"]) == 9 and d["pid"].isdigit():
                                        if d["ecl"] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                                            if (d["hgt"].endswith("cm") and 150 <= int(d["hgt"][:-2]) <= 193) or \
                                                    (d["hgt"].endswith("in") and 59 <= int(d["hgt"][:-2]) <= 76):
                                                count += 1

                d = {}  # reset
        else:
            if d:
                count_valid_fields = len(Day4.VALID_ENTRY_FIELDS.intersection(set(d.keys())))

                if count_valid_fields == length_valid_entry_fields \
                        or (count_valid_fields == (length_valid_entry_fields - 1) and "cid" not in d):
                    if 1920 <= int(d["byr"]) <= 2002 and len(d["byr"]) == 4:
                        if 2010 <= int(d["iyr"]) <= 2020 and len(d["iyr"]) == 4:
                            if len(d["eyr"]) == 4 and d["eyr"].isdigit() and 2020 <= int(d["eyr"]) <= 2030:
                                if d["hcl"].startswith("#") and len(d["hcl"]) == 7 and ishex(d["hcl"][1:]):
                                    if len(d["pid"]) == 9 and d["pid"].isdigit():
                                        if d["ecl"] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                                            if (d["hgt"].endswith("cm") and 150 <= int(d["hgt"][:-2]) <= 193) or \
                                                    (d["hgt"].endswith("in") and 59 <= int(d["hgt"][:-2]) <= 76):
                                                count += 1

        return count
