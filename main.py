from typing import List
import sys

import days


def main(args: List[str]):
    if not args:
        args = [input("Enter day to execute: ")]

    for arg in args:
        day = days.get_day(arg)

        if day:
            day.run()
        else:
            print(f"Could not find solution for Day {arg}.")


if __name__ == "__main__":
    main(sys.argv[1:])
